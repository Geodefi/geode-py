.. _internal_wallet:


Internal Wallet  
-----------------

    Every `operator` has an internal wallet. They use this wallet to create the ``Validator``.

.. py:method:: Portal.functions.increaseWalletBalance(id: uint256)

    Operators need 1 ethers to propose a validator. However, they get it back when theirs the proposal is approved.

.. WARNING::
    Please double-check you operator id before processing.

.. code-block:: python

    >>> transaction_params = {
        'to': Portal.address,
        'from': your_address,
        'value': web3.toWei(320, 'ether'),  # Example: sending 320 Ether for 10 Validator
        'gas': 200000,  # Example: setting the gas limit
        'gasPrice': web3.toWei('50', 'gwei')  # Example: setting the gas price
        }

    >>> transaction = Portal.functions.increaseWalletBalance(operatorId).buildTransaction(transaction_params)
    >>> signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)
    >>> tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)


.. py:method:: Portal.functions.decreaseWalletBalance(id: uint256, value: uint256)

    Like, above function, operators can also decrease their wallet balance.

.. code-block:: python

    ## It is not payable function.
    >>> transaction_params = {
        'to': Portal.address,
        'from': your_address,
        'gas': 200000,  # Example: setting the gas limit
        'gasPrice': web3.toWei('50', 'gwei')  # Example: setting the gas price
        }

    >>> transaction = Portal.functions.decreaseWalletBalance(operatorId, web3.toWei(320, 'ether')).buildTransaction(transaction_params)
    >>> signed_txn = web3.eth.account.sign_transaction(transaction, private_key=sender_private_key)
    >>> tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

