.. _utils:

Utils
==========

Validation
--------------

.. py:method:: createDepositData(mnemonics, mnemonic_password, start_index, num_keys):
    
    Parameters:
    ``mnemonics``: Space seperated list of words (string)
    ``mnemonic_password``: Any password (string)
    ``start_index``: start index of validators (uint)
    ``num_keys``: how many validators would you like to run (uint)

.. code-block:: python

    # Existing Mnemonic
    >>> mnemonics = "smooth satisfy legend glue aunt race rug sign core much enroll okay letter tragic coconut eyebrow unfold absurd wave brother fat roof weird found"
    >>> mnemonic_password = "12345678"
    >>> start_index = 0
    >>> num_keys = 1

    >>> createDepositData(start_index=start_index, mnemonics= mnemonics, mnemonic_password= mnemonic_password, num_keys = num_keys)

    # New Mnemonic
    >>> mnemonics = None

    >>> createDepositData(start_index=start_index, mnemonics= mnemonics, mnemonic_password= mnemonic_password, num_keys = num_keys)
    
    Mnemonics not provided. Generating new mnemonics...
    This is your mnemonic (seed phrase). Write it down and store it safely. It is the ONLY way to retrieve your deposit.

    rack verb venue either faculty spend initial trophy phrase moment wood denial robot vote glimpse scale section install snow rug pulse liberty curtain float

    Press any key when you have written down your mnemonic.


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
