.. _utils:


Utils
==========

MerkleTree
--------------


.. py:module:: Geode.utils.MerkleTree()
    

.. py:method:: generateTree(nodes: List[str], keccakTheLeaves = True):

    Generates merkle tree.

    Parameters:
    ``nodes`` :The abi encoded datasets of leaves
    ``keccakTheLeaves``: Did you provide hashes or byte data?

.. code-block:: python

    # Create Merkle Tree
    >>> tree  = MerkleTree()

    # Generate Tree
    >>> leaves = ['0xaa','0xbb','0xcc']
    >>> tree.generateTree(leaves)


.. py:method:: getProofs(leaf:str):

    Generates proofs of spesified leaf.

    Parameters:
    ``leaf`` : the leaf which intented to prove

.. code-block:: python

    # Arrange Leaves
    >>> tree.getProofs(leaves[0])



.. py:method:: printTree():

    Prints the tree to console.

.. code-block:: python

    >>> tree.printTree()
    # TODO

.. py:method:: root():

    Prints the ``root`` of the tree to console.

.. code-block:: python

    >>> tree.root
    '569d7dc1611b50e40d5b898c212f4742e3b7d76996bac5d63739fef589f3ccc0'
