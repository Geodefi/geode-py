.. _portal:


Portal
=============


.. py:module:: Geode.Portal

The ``portal`` module houses public utility functions from Portal contract.

Constants
------------

.. py:method:: portal.address

    Returns the ``address`` of the contract.

.. code-block:: python

    # get a Portal address
    >>> geode.Portal.address
    0xB0334F08dEC465Ec180F1AF04C6D7d3737407083


.. py:method:: PORTAL.contract.functions.CONTRACT_VERSION()

    Returns the ``CONTRACT_VERSION`` of the contract.

.. code-block:: python

    # get a Portal address
    >>> PORTAL.contract.functions.CONTRACT_VERSION().call()
    87373968589722757255522487689903791119558634447171488905970002736659167479131


.. py:method:: PORTAL.contract.functions.Do_we_care()

    Returns always ``True`` because we always care <3

.. code-block:: python

    # get a Portal address
    >>> PORTAL.contract.functions.Do_we_care().call()
    True



.. py:method:: PORTAL.contract.functions.GeodeParams()

    Returns address of ``SENATE``, address of ``GOVERNANCE``, integer of value of ``SENATE_EXPIRY`` and ``GOVERNANCE_FEE`` respectively.

.. code-block:: python

    # get a Portal address
    >>> PORTAL.contract.functions.GeodeParams().call()
    ['0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
    115792089237316195423570985008687907853269984665640564039457584007913129639935,
    0]


.. py:method:: PORTAL.contract.functions.StakingParams()

    Returns:
        ``VALIDATORS_INDEX``
        ``VERIFICATION_INDEX``
        ``MONOPOLY_THRESHOLD``
        ``EARLY_EXIT_FEE``
        ``ORACLE_UPDATE_TIMESTAMP``
        ``DAILY_PRICE_INCREASE_LIMIT``
        ``DAILY_PRICE_DECREASE_LIMIT``
        ``PRICE_MERKLE_ROOT``
        ``ORACLE_POSITION``

.. code-block:: python

    # get a Portal address
    >>> PORTAL.contract.functions.StakingParams().call()
    [10,
    9,
    115792089237316195423570985008687907853269984665640564039457584007913129639935,
    0,
    0,
    500000000, 
    500000000,
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C']


'getContractVersion',

.. py:method:: PORTAL.contract.functions.getContractVersion()

    Returns ``version`` of contract in integer.


.. code-block:: python

    # get a Portal address
    >>> PORTAL.contract.functions.getContractVersion().call()
    87373968589722757255522487689903791119558634447171488905970002736659167479131


Data Utils
-----------------

 'allIdsByType',

 'generateId',
 'getKey',
 'readAddressArrayForId',
 'readAddressForId',
 'readBytesArrayForId',
 'readBytesForId',
 'readUintArrayForId',
 'readUintForId',

 'getProposal',
 'getValidator',
 'getValidatorByPool',

Role Checks
-----------------

 'isAllowedModule',
 'isElector',
 'isMintingAllowed',
 'isPriceValid',
 'isPrisoned',
 'isPrivatePool',
 'isUpgradeAllowed',

Initiate Opeartor or Pool
-------------------------------
'getDefaultModule',
'getMaintenanceFee',


Oracle Utils
------------------------
 'updateVerificationIndex',
 'priceSync',
 'priceSyncBatch',
 'regulateOperators',
 'reportOracle',

Pausability
------------------------
 'pause',
 'pausegETH',
 'unpause',
 'unpausegETH',

Governance Only
------------------------

 'releasePrisoned',

 'setEarlyExitFee',
 'setElectorType',
 'setGovernanceFee',
 'setPoolVisibility',
 'setWhitelist',

 'changeIdCONTROLLER',
 'changeMaintainer',
 'changeSenate',
Wallet  
-----------------
 'decreaseWalletBalance',
 'increaseWalletBalance',

Executives Only
------------------------
 'approveOperators',
 'approveProposal',
 'approveSenate',

 'supportsInterface',
 'switchMaintenanceFee',
 'switchValidatorPeriod',


 'beaconStake',
 'blameOperator',
 'canStake',

 'deployLiquidityPool',
 'deposit',
 'fetchWithdrawalContractUpgradeProposal',
 'gETH',
 'gETHInterfaces',

 'initialize',
 'initiateOperator',
 'initiatePool',

 'newProposal',
 'onERC1155BatchReceived',
 'onERC1155Received',
 'paused',

 'proposeStake',

Updates  
-------
 'proxiableUUID',
 'upgradeTo',
 'upgradeToAndCall'
