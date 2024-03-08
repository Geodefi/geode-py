.. _staking_pool_handbook:

=====================
Staking Pool Handbook
=====================

Initilize a Customizable Staking Pool
-------------------------------------

Before Initiation
*****************
``32 Ether``
Creating a Pool is ``permissionless``, anyone can claim any pool name.
To prevent sybil attacks, initiation requires exactly 1 validator worth of funds. However, you can deposit more Ether later.

However, this amount will be used to create your first validator.

Pool ID 
************

Every Pool will have a ``unique`` ID.

It will be used for your Pool operations, and you can find your ID from both our frontend or Portal.


.. code-block:: python

    # First select a pool name. This name have to be unique.
    pool_name = 'Ice Pool'

    # Generate ID for your pool.
    >>> Portal.functions.generateId(pool_name, 5).call()
    54475916409245079355772281022530446651260021350020357005172842322230014479215


Initiate Your Pool!
**********************

**geodefi** uses an initiator function to set some parameters for your staking pool and derivative.

.. code-block:: python

    # First select a pool name. This name have to be unique.
    pool_name = 'Ice Pool'

    # Maintenance fee that will be charged for your services as the pool owner.
    # 10^10 represents 100%, can be set to up to 10% (10^9).
    # Can be changed later so lets assign 0.
    fee = 0

    # Middleware version https://docs.geode.fi/key-concepts/permissionless-configurable-staking-pools/current-middlewares
    # Middlewares are optional but select from above link.    
    middlewareVersion = 0
    middleware_data = ''

    # If you want to maintain
    maintainer = '0x<your-ethereum-address>'


    # config[0] = True if a private pool - Can be changed later.
    # config[1] = True if uses an middleware. Can not be changed later.
    # config[2] = True if uses a liquidity Pool - Can be changed later.
    config = [True, False, False ]

    # Dont forget to send with 32 ether.
    >>> tx = Portal.functions.initiatePool(
    pool_name,
    fee,
    middlewareVersion,
    maintainer,
    middleware_data,
    config
    ).buildTransaction(
        {
            'nonce': web3.eth.getTransactionCount(account.address)
            'value': web3.toWei(32, 'ether'),
            'from': account.address,
            'gas': gas_limit
        })

    # Sign with your private key
    >>> signed = w3.eth.account.sign_transaction(tx, private_key)

    # Send the transaction
    >>> tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)


Approve your Operators
***************************
Assume your balance is the number of validators within your pool. 
Your maintainer will be giving allowances to the Node Operators, and meanwhile, the Node Operators will compete to get as many validators as possible.
You can think of it as ERC-20 approvals. You are approving a certain amount of validators to be run by a Node Operator.

.. code-block:: python


    >> Portal.functions.approveOperators(
        pool_ID,
         [operatorIds],
         [allowances]
    )


Changing Your Pool's Owner
*****************************

CONTROLLER
The ``CONTROLLER`` key stands for the owner of the ID of a given staking pool.

After your pool is deployed you can get your pool:

.. code-block:: python

    # The id of pool
    poolID = 54475916409245079355772281022530446651260021350020357005172842322230014479215
    >> myPool = Portal.pool(poolID)

    ## How to get controller
    >> myPool.CONTROLLER
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'


Set a New Owner & Maintaner
***********************************************

At any given point, a Staking Pool can have 1 maintainer at most.

.. code-block:: python

    # Change the owner of the pool
    new_owner = '0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    >> Portal.function.changeIdCONTROLLER(poolID, new_owner)

    # Change the maintainer of the pool
    new_maintainer = '0xAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    >> Portal.function.changeMaintainer(poolID, new_maintainer)


    ## How to get controller
    >> myPool.CONTROLLER
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'

    ## How to get controller
    >> myPool.maintainer
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'


Changing Your Fee
***********************************************
.. code-block:: python

    ## It mean 1% (max 10%)
    new_fee = x * 10**10 /100 

    >> Portal.switchMaintenanceFee(pool_id, new_fee)


Claiming Your Fees
***********************************************
Every ID has an Internal Wallet, which makes transferring Ether easier for both Geode's Portal, and it's users.
The Internal Wallet is the place where your fees will accrue over time.

.. code-block:: python

    ## myPool = Portal.pool(pool_ID)
    wallet_balance = myPool.wallet  

    # Withdrawal 
    >> Portal.functions.decreaseWalletBalance(pool_ID, wallet_balance);


Making Your Pool Public or Private
***********************************************

Public Pools can be used by anyone
If you are a service provider willing to manage anyone's Ether, create a Public Pool. 

Private Pools can only be used by whitelisted addresses
If you are using a personal staking pool, or worried about KYC/AML, create a Private Pool.


.. code-block:: python

    # Making Your Pool Public
    >> Portal.functions.setPoolVisibility(pool_ID, False)
    # Making Your Pool Private
    >> Portal.functions.setPoolVisibility(pool_ID, True)

    # Set whitelist for your Private pool
    ## Whitelisted addressses
    contract_address = ['0xaa','0xaa','0xaa']
    >> Portal.functions.setWhitelist(pool_ID, contract_address)



Bound Liquidity Pool
***********************************************
You can also create a bound Liquidity Pool after initiation:

.. code-block:: python

    # For details
    # https://docs.geode.fi/key-concepts/bound-liquidity-pools
    >> Portal.functions.deployLiquidityPool(pool_ID)


