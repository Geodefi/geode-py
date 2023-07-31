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
    # TODO


Solidity
--------------

toBytes
.. py:method:: root():

    Prints the ``root`` of the tree to console.

.. code-block:: python

    >>> tree.root
    # TODO

toBytes32
.. py:method:: root():

    Prints the ``root`` of the tree to console.

.. code-block:: python

    >>> tree.root
    # TODO
toString
.. py:method:: root():

    Prints the ``root`` of the tree to console.

.. code-block:: python

    >>> tree.root
    # TODO
abiEncodepacked
.. py:method:: root():

    Prints the ``root`` of the tree to console.

.. code-block:: python

    >>> tree.root
    # TODO
intToHexString
.. py:method:: root():

    Prints the ``root`` of the tree to console.

.. code-block:: python

    >>> tree.root
    # TODO

Crypto
--------------

Wrappers
---------------


Id
--------------

.. py:method:: generateId(name: str, type: ID_TYPE):

    Generates an ID using keccak256 hash function.

    Parameters:
    ``name`` (str): The name used to generate the ID.
    ``type`` (ID_TYPE): The type of ID to generate.


.. code-block:: python

    # generate pool ID 
    >>> generateId(name = 'myPool', type = 5)
        87373968589722757255522487689903791119558634447171488905970002736659167479131



.. py:method:: getKey(id: int, key: str):

    Generates a key using keccak256 hash function.

    Parameters:
    ``id`` (int): The ID to use in generating the key.
    ``key`` (str): The key to generate.

.. code-block:: python

    # get surplus key of pool
    >>> getKey(id = 87373968589722757255522487689903791119558634447171488905970002736659167479131, key = 'surplus')
        79111955863444717148890597000273665916747913187373968589722757255522487689903