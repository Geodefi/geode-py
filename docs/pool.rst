.. _pool:

Pool
==========

.. py:module:: Pool
.. py:currentmodule:: Pool

.. contents:: :local:

Create a Pool Instance 
----------------------

.. py:method:: Geode.Portal.pool(poolID: int)

  Initilize the Pool object with an existing pool id:

  .. code-block:: python

    # You need pool id to create pool object
    poolID = 500191....78
    myPool = geode.Portal.pool(poolID)

Pool Ownership
--------------

.. py:property:: NAME

  ``NAME`` is the name of the pool that given from creator of the pool.

  .. code-block:: python

    myPool.NAME
    # Ice Pool

.. py:property:: CONTROLLER

  ``CONTROLLER`` ethereum address of the controller of the pool

  .. code-block:: python

    myPool.CONTROLLER
    # '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'

.. py:property:: initiated

  ``initiated`` (uint256) is timestamp of initiation time.

  .. code-block:: python

    myPool.initiated
    # 1677379164 
    # (unix seconds)

.. py:property:: maintainer

  ``maintainer`` (address) is the address of the maintainer, set by the owner. Handles day to day operations like delegation of deposited funds.

  .. code-block:: python

    myPool.maintainer
    # 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C

.. py:property:: yieldReceiver

  ``yieldReceiver`` (address) indicates the ethereum address of the reward collecter.

  .. WARNING::
    If the ``yieldReceiver`` is not set (or set to ``0x0000000000000000000000000000000000000000`` ), yield is distributed among token holders.

  .. code-block:: python

      myPool.yieldReceiver
      # 0x0000000000000000000000000000000000000000

Pool Configuration
------------------

.. py:property:: withdrawalCredential

  ``withdrawalCredential`` is used while creating the validators to propose. 
  
  .. warning:: 
    Using modified withdrawalContract is not a safe assumption.

  .. code-block:: python

    myPool.withdrawalCredential
    # 0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e

.. py:property:: withdrawalContract

  Any reward of the pool earns will be sent to this ``withdrawalContract`` ethereum address. According to Ethereum standards, this address is also at the end of the withdrawal credentials.

  .. code-block:: python

    myPool.withdrawalContract
    # 0xc82Ed5eC571673E6b18c4B092c9cbC4aE86C786e

.. py:property:: whitelist

  Sometimes some maintainers may want to define a ``whitelist`` for the pool. In this case, you can see it with the whitelist command. If there is no white list, you will see ``0x0000000000000000000000000000000000000000`` address.

  .. code-block:: python

    myPool.whitelist
    # 0x0000000000000000000000000000000000000000

.. py:property:: liquidityPool

  Address of the ``liquidityPool``.

  .. code-block:: python

    myPool.liquidityPool
    # 0xEC5B756326f161bdc6506c16800ddF56765E0f3b

  .. NOTE::

    Not all pools have whitelist or liquidityPool features.

.. py:property:: private

  ``private`` is the boolean value to either the pool is prived pool or public pool.

  .. code-block:: python

    myPool.private
    # False

Pool Fee
----------------------

.. py:property:: fee

  Returns ``fee`` (uint256) How much of the percentage from validator yield will received by the pool owner. DENOMINATOR: 1e10 (100%).

    .. code-block:: python

      myPool.fee
      # 500000000
      # PERCENTAGE_DENOMINATOR = 100%

  .. NOTE::
      If the pool owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the pool momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave the pool according to their own interests.

.. py:property:: priorFee

  ``priorFee`` replaces ``fee`` when ``feeSwitch`` is reached.

  .. code-block:: python

    myPool.priorFee    
    # 400000000
    # PERCENTAGE_DENOMINATOR = 100%

.. py:property:: feeSwitch

  ``feeSwitch`` is set to 3 days after the function call, meaning there will be 3 days delay on every time fee is changed.

  .. code-block:: python

    myPool.feeSwitch
    # 1709191201
    # (unix seconds)

ERC20 Tokens (middlewares)
--------------------------

.. py:method:: middlewaresList

    ``middlewaresList`` list of (address)es 

    .. WARNING::
      To avoid malfunctions, utilizing our standard middlewares is expected by the pool owners.

    .. code-block:: python

      myPool.middlewaresList()
      # ['0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3']

.. py:method:: middlewares(index: uint256)

  ``middlewares`` returns you the middleware corresponding to the given index. If the index is too large, it will throw an error.

  .. code-block:: python

    myPool.middlewares(0)
    # 0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3

.. py:property:: middlewaresLen
    
  ``middlewaresLen`` returns the length of the middlewaresList. If you want to achieve multiple middlewares, it can be used to set the limits of the loop before executing the above code.

  .. code-block:: python

    myPool.middlewaresLen
    # 1

Operator Marketplace
---------------------

.. py:method:: allowance(operatorId: int)

  ``allowance`` allowance's of the operators that given ID.

  .. code-block:: python

    myOperator = geode.Portal.operator(operatorID)
    myPool.allowance(operator=myOperator.ID)
    ## 12

.. py:method:: validators(index:uint256)

  ``validators`` Returns the pubkey of the validator corresponding to the given index.

  .. code-block:: python

    ## In bytes
    print("Pubkey:",myPool.validators(0))
    
    Pubkey: b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'

    ## In hex string
    print("Pubkey:", myPool.validators(0).hex())

    Pubkey: '9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d'

.. py:property:: validatorsList

  Returns ``validatorsList`` (List(bytes32)) All validator pubkeys that registered to this pool.

  .. code-block:: python

    myPool.validatorsList
    # [b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d']

.. py:property:: validatorsLen

  ``validatorsLen`` (uint256) number of validators in the pool. Size of validatorsList array.

  .. code-block:: python

    myPool.validatorsLen
    # 1

.. py:method:: activeValidators(operatorId: int)

  ``activeValidators`` Number of validators that currently active, according to Portal.

  .. code-block:: python

    myOperator = geode.Portal.operator(operatorID)
    myPool.activeValidators(operator=myOperator.ID)
    
  .. NOTE::
      More than one operator can work in a pool. And each operator will have their own validators. You can get this information with the operator's ID.

.. py:method:: proposedValidators(operatorId: int)

  ``proposedValidators`` Number of validators that not active, but waiting to be activated, according to Portal.

  .. code-block:: python

    myOperator = geode.Portal.operator(operatorID)
    myPool.proposedValidators(operator=myOperator.ID)
    

.. py:method:: alienValidators(operatorId: int)

  ``alienValidators``  Number of validators that are dedected as faulty, according to Oracle.

  .. code-block:: python

    myOperator = geode.Portal.operator(operatorID)
    myPool.alienValidators(operator=myOperator.ID)
  
Staking Related Data
----------------------

.. py:property:: surplus

  ``surplus`` (uint256) amount that is waiting to be delegated (useful when proposing a validator). 

  .. code-block:: python

    myPool.surplus
    # 1000000000000000000

.. py:property:: secured

  ``secured`` (uint256) amount that is reserved, and waiting to be sent to validators with approved proposals.

  .. code-block:: python

    myPool.secured
    # 1000000000000000000

Internal Wallet
-------------------

.. py:property:: wallet

  | Every ID has its own internal wallet within Portal. 
  | It accrues fees, makes things safer and easier for Node Operators when creating validators etc. 
  | ``wallet`` (uint256) amount (in ``wei``) in the internal wallet of the pool
  
  .. code-block:: python

    print("wallet:",myPool.wallet)
    # wallet: 10000000000000
    # (as wei) (1e18 = 1 ether)

  .. note:: 
    | ``CONTROLLER`` of an ID can increase the internal wallet by depositing ether with ``portal.functions.increaseWalletBalance(id)``.
    | Also, can decrease by reclaiming the ether that is accrued with ``portal.functions.decreaseWalletBalance(id)``.

Fallback Operator
----------------------

.. WARNING::

    Fallback Operator mechnanism is for advanced users. Most of the applications, will not need these functionalities.

.. py:property:: fallbackOperator

  ``fallbackOperator`` (uint256) is the ID of selected Operator as ``fallback``.

  .. code-block:: python

    myPool.fallbackOperator
    # 500191....78
    
.. py:property:: fallbackThreshold

  ``fallbackThreshold`` (uint256) means when ``fallbackThreshold``% of allowances are filled, ``fallbackOperator`` will have unlimited allowance.

  .. code-block:: python

    print("fallbackThreshold:",myPool.fallbackThreshold)
    # 800000000000
    # 80% as PERCENTAGE_DENOMINATOR = 100%

More 
-------

Next step: Checkout :ref:`staking_pool_handbook`.
