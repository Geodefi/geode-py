.. _pools:

Pools 
==========

Initilization
--------------------------------------------------
.. py:method:: Geode.Portal.pool(poolID: int)

Initilize the Pool object of Geode.

.. code-block:: python

    >> geode = Geode(exec_api, cons_key)
    ## You need pool id to create pool object
    >> poolID = 500191....78
    >> myPool = geode.Portal.pool(poolID)


General Information of Pool
----------------------------------

NAME
******************

``NAME`` is the name of the pool that given from creator of the pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("NAME:",myPool.NAME)
    NAME: Ice Pool


CONTROLLER
----------------

``CONTROLLER`` ethereum address of the controller of the pool


.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    ##'0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'
    >> print("CONTROLLER:", myPool.CONTROLLER)
    CONTROLLER: '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'

initiated
--------------------------------------------------

``initiated`` (uint256) is the name of the pool that given from creator of the pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("initiated:",myPool.initiated)
    initiated: 1677379164

maintainer
--------------------------------------------------

``maintainer`` (address) is the address of the maintainer.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("maintainer:",myPool.maintainer)
    
    maintainer: 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C

liquidityPool
--------------------------------------------------

    Address of the ``liquidityPool``.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("whitelist:",myPool.liquidityPool)
    
    liquidityPool: 0xEC5B756326f161bdc6506c16800ddF56765E0f3b


private
--------------------------------------------------

``private`` is the boolean value to either the pool is prived pool or public pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("private:",myPool.private)
    
    private: False


Wallet
*******************

surplus
--------------------------------------------------

``surplus`` (uint256) shows the surplus ether amount of the pool. 

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("surplus:",myPool.surplus)
    
    surplus: 1000000000000000000



secured
--------------------------------------------------

``secured`` (uint256) shows the guaranteed ether amount of the pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("secured:",myPool.secured)
    
    secured: 1000000000000000000



Interfaces
************************************

interfacesList
--------------------------------------------------

``interfacesList`` list of (address)es 
    Although we expect pools to generally use our standard interfaces, they are free with interfaces and geode supports multiple interfaces. You can easily build on the standards.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("interfacesList:",myPool.interfacesList)
    
    interfacesList: ['0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3']


interfaces(index:uint256)
--------------------------------------------------

``interfaces`` returns you the interface corresponding to the given index. If the index is too large, it will throw an error.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("interfaces:",myPool.interfaces(0))
    
    interfaces: '0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3'


interfaces(index:uint256)
--------------------------------------------------

``interfaces`` returns you the interface corresponding to the given index. If the index is too large, it will throw an error.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("interfaces:",myPool.interfaces(0))
    
    interfaces: '0xdaED82d9a6a0282D9084375eb1Dc8c09440e2aB3'

interfacesLen
--------------------------------------------------

``interfaces`` returns the number of interfaces. If you want to achieve multiple interfaces, it can be used to set the limits of the loop before executing the above code.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("interfacesLen:",myPool.interfacesLen)
    
    interfacesLen: 1


Withdrawal Data
********************************

withdrawalCredential
--------------------------------------------------

``withdrawalCredential`` means that every validator working for this pool will receive their ether earned money to this address. The accuracy of this data is always checked by the Geode so that the Pool is not damaged.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("withdrawalCredential:",myPool.withdrawalCredential)
    
    withdrawalCredential: 0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e

withdrawalContract
--------------------------------------------------

Any money the pool earns will be sent to this ``withdrawalContract`` ethereum address. According to Ethereum standards, this address is also at the end of the withdrawal credentials.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("withdrawalContract:",myPool.withdrawalContract)
    
    withdrawalContract: 0xc82Ed5eC571673E6b18c4B092c9cbC4aE86C786e



whitelist
--------------------------------------------------

Sometimes some maintainers may want to define a ``whitelist`` for the pool. In this case, you can see it with the whitelist command. If there is no white list, you will see 0x0000000000000000000000000000000000000000 address.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("whitelist:",myPool.whitelist)
    
    whitelist: 0x0000000000000000000000000000000000000000

Fee
**********************************************

If the pool owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the pool momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave the pool according to their own interests.


fee
--------------------------------------------------

``fee``(uint256) How much commission the pool will take? DENOMINATOR: 1e9

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("fee:",myPool.fee)
    
    fee: 500000000

priorFee
--------------------------------------------------

``priorFee`` replaces ``fee`` in ``feeSwitch`` period.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("whitelist:",myPool.priorFee)
    
    priorFee: 0

feeSwitch
--------------------------------------------------

``feeSwitch`` is the block period, corresponds to 3 days.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("feeSwitch:",myPool.feeSwitch)
    
    feeSwitch: 0



Validators
********************************


validatorsList
--------------------------------------------------

``validatorsList``(List(bytes32)) All validator pubkeys that registered to this pool.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("validatorsList:",myPool.validatorsList)
    
    validatorsList: [b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d']


validatorsLen
--------------------------------------------------

``validatorsLen`` (uint256) number of validators in the pool. Size of validatorsList array.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> print("validatorsLen:",myPool.validatorsLen)
    
    validatorsLen: 1


validators(index:uint256)
--------------------------------------------------

``validators`` Returns the pubkey of the validator corresponding to the given index.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    ## In bytes
    >> print("Pubkey:",myPool.validators(0))
    
    Pubkey: b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'

    ## In hex string
    >> print("Pubkey:", myPool.validators(0).hex())

    Pubkey: 9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d


Operators
****************************************

More than one operator can work in a pool. And each operator will have their own validators. You can get this information with the operator's ID.


activeValidators
--------------------------------------------------

``activeValidators`` Validator pubkeys that currently operating.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("activeValidators:",myPool.activeValidators(operator=myOperator.ID))
    

activeValidators
--------------------------------------------------

``activeValidators`` Validator pubkeys that currently operating under the opeartor.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("activeValidators:",myPool.activeValidators(operator=myOperator.ID))
    

proposedValidators
--------------------------------------------------

``proposedValidators`` Validator pubkeys that are proposed by the operator.

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("activeValidators:",myPool.proposedValidators(operator=myOperator.ID))
    


allowance
--------------------------------------------------

``allowance`` allowance's of the operators that given ID.


.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> myOperator = geode.Portal.operator(operatorID)
    >> print("allowance:",myPool.allowance(operator=myOperator.ID))

