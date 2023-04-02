from math import pow, ceil, log2
from functools import cache
from .crypto import keccak256
from .solidity import intToHexString, abiEncodepacked


class MerkleTree:

    def __init__(self, sort=True):
        """
        The merkle tree works like a heap array.
        In the worst case scenario, there is O(nlogn) memory complexity,
        but heap array is preferred because it can be implemented more easily.
        It only works with keccak256 and is compatible with Solidity.

        param:sort == Two child node will be sorted when concatting to get hash of parent Default:True
        """
        self._tree = []
        self._generated = False

        self._depth = 0  # 0 or 1 nodes => 0 depth, 2 nodes => 1 depth, 4 nodes => 2 depth,
        self._numberOfNodes = 0  # The lenght of leaves

        # Always power of 2, How many memory should be allocated.
        self._sizeOfTree = 0
        self._sort = sort  # Recommentation: Always use sort = True for solidity compatilibty

    def generateTree(self, nodes, keccakTheLeaves=True):
        """
        Hash every node with keccak until the root has been calculated.
        Always first index of the tree is None (tree[0] = None)
        If the nodes is not power of 2, None type nodes will be generated.
        Some parents nodes will be None also.

        Tree Structure:
                Root:    tree[1]
                        /      |
                     tree[2]    tree[3]
                    /      |    /      |
             tree[4] tree[5]  tree[6]  tree[7]
                        ...

        How to handle None types (Notice (tree[6] == tree[3]))

                Root:    H( H(0xaa.., 0xbb..) , 0xcc..)
                        /                   |
                H(0xaa.., 0xbb..)           0xccc...    
                    /      |                /       |
              0xaaa.. 0xbbb..          0xccc..      None

        param:keccakTheLeaves == If true: the leaves (nodes) will also be hashed.
        Otherwise, tree assumes you submit the hex-string which result of some hashes as leaves
        Default: True
        """

        # If empty do not change anything
        if not nodes:
            return

        numberOfNodes = len(nodes)  # Lets assume numberOfNodes is 13,
        # Then, the tree size will be 32, so depth will be 5
        depth = 1 + ceil(log2(numberOfNodes))
        sizeOfTree = int(pow(2, depth))

        self._tree = [None] * sizeOfTree
        self._sizeOfTree = sizeOfTree
        self._depth = depth
        self._numberOfNodes = numberOfNodes

        # Right half of the list is always leaves
        # Right half of the left half is Layer 1
        # Right half of the right half of the left half is Layer 2..
        # Tree: [None] [Root]. [][]. [][][][]. [][][][][][][][]
        #               Root  Layer2  Layer1       Leaves

        startIndex = sizeOfTree//2

        # First Insert Leaves

        # Did you have only the hashes then keccakTheLeaves must be False
        if keccakTheLeaves:
            for i, node in enumerate(nodes):
                self._tree[i + startIndex] = self._keccak256(node)
        else:
            for i, node in enumerate(nodes):
                self._tree[i + startIndex] = node

        # Generate Upper Layers
        while startIndex >= 1:
            startIndex //= 2  # Traverse like ...32 - 16 - 8 - 4 - 2 - 1

            for i in range(startIndex):
                left = self._tree[(i + startIndex)*2]
                right = self._tree[(i + startIndex)*2 + 1]

                if (right is None and left is None):
                    self._tree[i + startIndex] = None
                elif (left is None):
                    self._tree[i + startIndex] = right
                elif (right is None):
                    self._tree[i + startIndex] = left
                else:
                    self._tree[i + startIndex] = self._keccak256(
                        self.concat(left, right, self._sort))

        self._generated = True

    def getProofs(self, leaf):
        """
        Tree Structure:
                Root:    tree[1]
                        /      |
                     tree[2]    tree[3]
                    /      |    /      |
             tree[4] tree[5]  tree[6]  tree[7]
                        ...

        Sample:
                leaf = tree[4]
                returns = [tree[5], tree[3]]

        If you generate proofs by tree[4],,
            tree[5] and tree[3] can re-generate the root like
            H(tree[4], tree[5]) (which is equal to tree[2])

            and 
            H(tree[2], tree[3]) can re-generate the tree[1] which is ROOT


        :param: leaf => get some node hashes which can re-generate the root
                If leaf is not in the tree raise Exception
        """

        proofList = []
        indexOfNode = 0

        # Search within the right half of the tree
        for i in range(self.sizeOfTree//2, self.sizeOfTree):
            if (self._tree[i] == leaf):
                indexOfNode = i
                break

        # If you could not find the leaf
        if indexOfNode == 0:
            raise Exception(f'{leaf} is not a leaf')

        while True:
            # Get sibling of the node
            # Sibling == If odd, substract 1, if even, add 1.
            # Sample siblings: (4,5), (45,44), (1245125, 1245124)
            proof = self._tree[
                indexOfNode + 1] if i % 2 == 0 else self._tree[
                    indexOfNode - 1]

            proofList.append('0x'+proof)
            # Divide 2 means go to parent node
            indexOfNode //= 2

            if (indexOfNode == 1):
                break

        return proofList

    def verifyProof(self, leaf, proofs) -> bool:
        # To be Implemented
        pass

    def printTree(self):
        if self.generated:
            print("============== TREE ==============")

            self.nextNode(1)

    @cache
    def nextNode(self, i):
        if i > self._sizeOfTree - 1:
            return

        depthOfIndex = int(log2(i)) + 1

        if self._tree[i] is None:
            pass
        else:
            print(i, '|  ' * depthOfIndex + '|'+'_' *
                  depthOfIndex + ': ' + self._tree[i])

        # RECURSION
        self.nextNode(i*2)
        self.nextNode(i*2 + 1)

    @staticmethod
    def _keccak256(message: str) -> str:
        """
        Keccak256 of the message.
        First the message will be converted to bytes 
        """

        return keccak256(message)

    @staticmethod
    def _intToHexString(number: int) -> str:
        """
        integer to hex string
        :param number: the number to convert

        31 -> "(0x)000000000000000000000000000000000000001f"
        """
        return intToHexString(number)

    @classmethod
    def _abiEncodepacked(cls, *args) -> str:
        """
        Functions as abi.encodePacked() in Solidity
        Takes any number of integer arguments converts to hex integers and pad '0's to beginning.
        returns bytes32 string

        Sample:
        0 => 0x0000000000000000000000000000000000000000000000000000000000000000
        721077 => 0x00000000000000000000000000000000000000000000000000000000000b00b5
        31, 64206, 1309 => 0x00000001f000000000000000000000000000000000000000000000000000000000000face000000000000000000000000000000000000000000000000000000000000051d
        """

        return abiEncodepacked(args)

    @staticmethod
    def concat(a: str, b: str, sort=True) -> str:
        """
        concat two strings like

        0xAAA + 0xBBB => 0xAAABBB

        param a: first string
        param b: first string
        param sort: if True, sort the strings before concatting, Default: True
        """

        if not isinstance(a, str) or not isinstance(b, str):
            raise ValueError("concat function works with strings")

        if len(a) > 2 and a[:2] == '0x':
            a = a.lstrip('0x')

        if len(b) > 2 and b[:2] == '0x':
            b = b.lstrip('0x')

        if sort:
            return ('0x' + a + b) if a < b else ('0x' + b + a)
        else:
            return ('0x' + a + b)

    def __str__(self):
        return f"The tree has no leaves yet." if not self._generated else f"Tree Root Hash: {self.root}"

    def reset(self):
        """
        Clear the list.
        """
        self._tree = []
        self._generated = False
        self._depth = 0
        self._sizeOfTree = 0
        self._numberOfNodes = 0

    # Properties

    @property
    def root(self):
        if not self._generated:
            print('WARNING! The Merkle Tree is not generated yet.')
            return '0x'
        return self._tree[1]

    @property
    def generated(self):
        return self._generated

    @property
    def numberOfNodes(self):
        return self._numberOfNodes

    @property
    def tree(self):
        return self._tree[1:]

    @property
    def sizeOfTree(self):
        return self._sizeOfTree

    @property
    def depth(self):
        return self._depth

    @property
    def leaves(self):
        self._tree[len(self._tree)//2:]
