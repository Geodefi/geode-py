.. _signatures:

Signatures 
==============

.. py:method:: DepositData()

.. code-block:: python

    # get a Portal address
    >>> class DepositData(Serializable):
            fields = [
            ('pubkey', bytes48),
            ('withdrawal_credentials', bytes32),
            ('amount', uint64),
            ('signature', bytes96)
            ]


.. py:method:: DepositMessage()

.. code-block:: python

    # get a Portal address
    >>> class DepositMessage(Serializable):
            """
            Ref: https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md#depositmessage
            """
            fields = [
                ('pubkey', bytes48),
                ('withdrawal_credentials', bytes32),
                ('amount', uint64),
            ]


.. py:method:: validate_deposit()


.. code-block:: python

    # get a Portal address
    >>> depositData = DepositData(
        pubkey = '',
        withdrawal_credentials = '',
        amount = DEPOSIT_SIZE.BEACON,
        signature = '',
        deposit_data_root = '0x',
        fork_version = '0x',
        )
    
    >>> validate_deposit(depositData)
    True


.. py:method:: validate_deposit_data_file()


.. code-block:: python

    # get a Portal address
    
    >>> validate_deposit_data_file(
        deposit_data_path="deposit_data/**.json",
        amount=DEPOSIT_SIZE.BEACON,
        credential="01000000000000000000000095222290dd7278aa3ddd389cc1e1d165cc4bafe5",
        network= Network.ethereum
        )