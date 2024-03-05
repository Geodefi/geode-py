.. _internal_wallet:

Internal Wallet  
===============

    | ``wallet`` (uint256) amount (in ``wei``) in the internal wallet of the Operator.
    | Every ID has its own internal wallet within Portal. It accrues maintanence fees, makes things safer and easier for Node Operators when creating validators etc. 

.. note::     
    | Validator proposals requires 1 Ether, which will be spent from your internal wallet.
    | However, this amount is returned if the proposal is approved and the validator creation is finalized.

.. py:method:: Portal.functions.increaseWalletBalance(id: uint256)

    Increases internal wallet by accepting the deposited ETH amount.

.. WARNING::
    | You will need to provide a private key and setup your wallet with provided web3 instance to send any transactions:
    | :ref: `Setting up your wallet with PRIVATE_KEY` 

    .. code-block:: python

        # Example: sending 320 Ether for 10 Validator
        amount = portal.w3.toWei(320, 'ether')  

        transaction_params = {
            'from': acct.address, # no need if defaultAccount is set 
            'value': amount,
            'gas': 200000,  # Example: setting the gas limit
            'gasPrice': web3.toWei('50', 'gwei')  # Example: setting the gas price
        }

        # Returns the tx hash as HexBytes
        tx_hash = portal.functions.increaseWalletBalance(myOperator.ID).transact(transaction_params)
        # HexBytes('0xed0389fb5f45d676808d7a72ccb694d989f39495e2e6911c39ce4253cf976e34')

.. py:method:: Portal.functions.decreaseWalletBalance(id: uint256, value: uint256)

    Like, above function, operators can also decrease their wallet balance.

    .. code-block:: python
        
        # Example: withdrawing 320 eth back
        amount = portal.w3.toWei(320, 'ether') 

        transaction_params = {
            'from': acct.address, # no need if defaultAccount is set 
            'value': 0,
            'gas': 200000,  # Example: setting the gas limit
            'gasPrice': web3.toWei('50', 'gwei')  # Example: setting the gas price
        }

        # Returns the tx hash as HexBytes
        tx_hash = portal.functions.decreaseWalletBalance(myOperator.ID, amount).transact(transaction_params)
        # HexBytes('0xed0389fb5f45d676808d7a72ccb694d989f39495e2e6911c39ce4253cf976e34')