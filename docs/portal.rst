.. _portal:


======
Portal
======

.. py:module:: Portal
.. py:currentmodule:: Portal

.. py:class:: geodefi.Portal

Provides easy access to the public utility functions for the **main smart contract** of the staking infrastructure: Portal. 

.. contents:: :local:

----

----------------
Class Attributes
----------------

    .. py:attribute:: Portal.address

        Returns the ``address`` of the contract.

    .. code-block:: python

        geode.portal.address
        # 0xB0334F08dEC465Ec180F1AF04C6D7d3737407083
        

    .. py:attribute:: Portal.version

        Returns the current ``version`` of the contract.

    .. NOTE:: 
        geodefi smart contracts has their own built-in version management system based on UUPS.
        This ``version`` should not be confused with smart contract's proxy version, which increases by one on every update.

    .. code-block:: python

        geode.portal.version
        #96496677624318398099812318321560460756447703796250258508740352959269719433552    

        from geodefi.utils import to_bytes32, to_string

        # read as a string: 
        version_name = geode.portal.functions.readBytes(self.version, to_bytes32("NAME")).call()

        # convert from bytes to string: 
        to_string(version_name)
        # v1_0

    .. py:attribute:: Portal.network

        Returns the ``network`` of the contract as a ``geodefi.Network`` (strEnum) instance.

    .. code-block:: python

        geode.portal.network
        # <Network.holesky: 17000>    

----

---------
Functions
---------

    .. code-block:: python

        # recommended for easier access:
        portal = geode.portal

    .. NOTE:: 
        On Portal and Token instances, contracts can be utilized with ``instance.contract.functions.name().call()`` .
        However, similarly can be accessed through: ``instance.functions.name().call()`` , which removes the useless ``contract`` in the middle.

Parameters
----------

    .. py:method:: GeodeParams()

            * ``governance`` : proposer part on the dual governance
            * ``senate`` : authority that approves the proposers
            * ``approvedUpgrade`` : special proposal that is approved by the senate. Contract can be upgraded to given instance afterwards.
            * ``senateExpiry`` : a senate can only function for 365 days max. Governance should propose a new senate before the circuit-breaker is activated.
            * ``packageType`` : portal's package TYPE is 10001. Similarly, other packages such as withdrawal contract etc. also has ID_TYPE between ``10000-19999``.

    .. code-block:: python

        portal.functions.GeodeParams().call()
        # ['0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
        # '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
        # '0x6699580E23Fc6a802e996a654845348CA560bc94',
        # 1717847448,
        # 10001]


    .. py:method:: StakeParams()

            * ``gETH`` : deployed token address
            * ``oraclePosition`` : geoscope oracle multisig address 
            * ``validatorsIndex`` : current index of the validators, includes all states.
            * ``verificationIndex`` : verified validators, only increases as more validators are evaluated. Note that, not all evaluated validators are verified.
            * ``monopolyThreshold`` : given ``PERCENTAGE_DENOMINATOR = 100%``, max amount of validators of a operator can be up to x% of the all validators on the beaconchain.
            * ``beaconDelayEntry`` : a validator proposal can be delayed up to x seconds (currently represents 14 days) by the operator.
            * ``beaconDelayExit`` : a validator exit request can be delayed up to x seconds (currently represents 14 days) by the operator.
            * ``initiationDeposit`` : Fixed amount that should be deposited  to reserve a NAME while creating a staking pool (currently 32 eth).
            * ``oracleUpdateTimestamp`` : timestamp for the latest oracle update, which set new merkle roots.
            * ``dailyPriceIncreaseLimit`` : price of the token can decrease x% * elapsed_days at most.
            * ``dailyPriceDecreaseLimit`` : price of the token can increase x% * elapsed_days at most.

    .. code-block:: python

        portal.functions.StakeParams().call()
        # ['0xaA970005F693Ae459e0ee107c63b546E8ff51d5d',
        # '0x7B6fA217a374826FCa50dccB87041AE0e34Ba1f5',
        # 0,
        # 0,
        # 0,
        # 1209600,
        # 1209600,
        # 32000000000000000000,
        # 0,
        # 700000000,
        # 700000000]


    .. py:method:: getContractVersion()

        Returns ``version`` of contract in integer.


    .. code-block:: python

        portal.functions.getContractVersion().call()
        # 87373968589722757255522487689903791119558634447171488905970002736659167479131


Isolated Storage
----------------

    .. image:: storage.png
        :width: 300
        :alt: Isolated Storage Layout

    DataStore is designed to host multiple parties of different ``TYPE`` entities, without them affecting each other's storage space under any condition.

    This is achieved by utilizing ``id`` and ``key`` pairs within the storage.

    .. note:: 
        DataStore can only store 3 types of variables: UINT256, Address, Bytes. Worth noting, DataStore not only can store these types, but can also store Arrays of these types and relational data between different IDs by generating a new key for the unqiue combinations.

    .. NOTE::
        Do not forget to call the correct function according to the type of the variable you will return.

    .. WARNING::
        We recommend that you initialize the ``Pool``, ``Operator`` or ``Validator`` and read the data that way, instead of calling it from the ``Portal`` directly. 
        See :doc:`Pools <pool>`, :doc:`Operators <operator>`, :doc:`Validators <validator>`,

    .. py:method:: readBytes(id : uint256, key : bytes32)

    .. code-block:: python

        from geodefi.utils import to_bytes32, to_string
        pid = 29228457249232120346521013786824808088246537603535847808963148138747123868265
        
        name = portal.functions.readBytes(pid, to_bytes32("NAME")).call()
        # b'Icy Pool'

        to_string(name)
        # 'Icy Pool'

    .. py:method:: readAddress(id : uint256, key : bytes32)

    .. code-block:: python

        from geodefi.utils import to_bytes32, to_string
        pid = 29228457249232120346521013786824808088246537603535847808963148138747123868265
        
        address = portal.functions.readAddress(pid, to_bytes32("CONTROLLER")).call()
        # 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C



    .. py:method:: readUint(id : uint256, key : bytes32)

    .. code-block:: python

        from geodefi.utils import to_bytes32, to_string
        pid = 29228457249232120346521013786824808088246537603535847808963148138747123868265
        
        address = portal.functions.readUint(pid, to_bytes32("fee")).call()
        # 5e8 # equal to 5%

Arrays
******

    .. NOTE::
        If you want to get lenght of the array you can call ``readUint`` function with the same ``key`` like below function.

    .. code-block:: python
        
        # length
        portal.functions.readUint(pid, to_bytes32("middlewares")).call()
        # 3
        
        # index
        portal.functions.readAddressArray(pid, to_bytes32("middlewares"), index).call()
        # 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C

    .. py:method:: Portal.functions.readBytesArray(id : uint256, key: bytes32, index: uint256)

    For getting array of ``bytes``.

    .. py:method:: Portal.functions.readAddressArray(id : uint256, key: bytes32, index: uint256)

    For getting array of ``address``.

    .. py:method:: Portal.functions.readUintArray(id : uint256, key: bytes32, index: uint256)

    For getting array of ``uint256``.


List of all IDs 
---------------

    .. py:method:: Portal.functions.allIdsByType(type: uint256, index: uint256)

        Returns the ``id`` of specific type of given index.
        
    .. code-block:: python

        from geodefi.globals import ID_TYPE

        # Get Pools (ID_TYPE => 5)
        portal.functions.allIdsByType(ID_TYPE.POOL,0).call()
        # 29228457249232120346521013786824808088246537603535847808963148138747123868265
        portal.functions.allIdsByType(5,0).call()
        # 29228457249232120346521013786824808088246537603535847808963148138747123868265
    
        portal.functions.allIdsByType(ID_TYPE.POOL,99).call()
        # ContractLogicError

        # Get Operators (ID_TYPE => 4)
        portal.functions.allIdsByType(ID_TYPE.OPERATOR,0).call()
        114391297015478800753082638170652680401082080549997516459063441314156612391510
        portal.functions.allIdsByType(4,0).call()
        114391297015478800753082638170652680401082080549997516459063441314156612391510


    .. py:method:: Portal.functions.allIdsByTypeLength(type: uint256)

        Returns the ``lenght`` of specific type of given index.
        
    .. code-block:: python

        from geode.globals import ID_TYPE

        # Get Pool IDs Length (ID_TYPE => 5)
        portal.functions.allIdsByTypeLength(ID_TYPE.POOL).call()
        # 13

        # Get Operator IDs Length (ID_TYPE => 4)
        portal.functions.allIdsByTypeLength(ID_TYPE.OPERATOR).call()
        # 5


Generating IDs and KEYs
-----------------------

Local (recommended)
*******************

    Utilize utils functions:

    .. code-block:: python

        from geode.utils import generate_id, get_key

        id = generate_id("Some_Pool", 5)
        # 76326158993240509638979169100046752960475693436338829808324780012712985408415

        get_key(id, "array_name")
        # HexBytes('0x1a4666a7056a1f68c5a72f124ff88dd31ad1576baf1633657754e387e30a2b2b')

Onchain
*******

    .. py:method:: Portal.functions.getKey(id: uint256, param: bytes32)

        returns Bytes.

    .. code-block:: python

        portal.functions.getKey(poolID, to_bytes32('CONTROLLER')).call()
        # b'\xb4s\xca\xe0\xf2\xd9\xf2!*k\xfd$\xd9\xff\xcc\n\xf8\xcc7>\xae{=\x8f&\xb9\xbe\xc6_\x00^\xdf'

    .. py:method:: Portal.functions.generateId(name: string, type: uint256)

        returns uint256.

    .. code-block:: python

        portal.functions.generateId("Some_Pool", 5).call()
        # 97770474815149397909782741678802560703260876453812799861980400297568557242506


Other View Functions for Pools, Operators and Validators
--------------------------------------------------------------
.. py:method:: Portal.functions.canStake(pubkey: bytes)

    ``True`` if the validator of given pubkey passed the checks and is ready to stake, ``False`` otherwise.

    .. code-block:: python

        ## pubkey: bytes
        portal.functions.canStake(pubkey).call()
        True

.. py:method:: Portal.functions.isMiddleware(_type: uint256, version: uint256)

    ``True`` if list of middlewares for given type ``ID_TYPE`` (e.g ``MIDDLEWARE_GETH = 20011``) has provided version set as a middleware on portal, that can be used while pool creation.

    .. code-block:: python

        portal.functions.isMiddleware(ID_TYPE.MIDDLEWARE_GETH, 97770474815149397909782741678802560703260876453812799861980400297568557242506).call()
        # False

.. py:method:: Portal.functions.getPackageVersion(_type: uint256, version: uint256)

    Returns the latest version for given ``ID_TYPE`` (e.g ``PACKAGE_WITHDRAWAL_CONTRACT = 10011``) :

    .. code-block:: python

        _v =portal.functions.getPackageVersion(ID_TYPE.PACKAGE_WITHDRAWAL_CONTRACT).call()
        # 97770474815149397909782741678802560703260876453812799861980400297568557242506
        
        # get version's name as a string: 
        _v_name = portal.functions.readBytes(_v, to_bytes32("NAME")).call()

        # convert from bytes to string: 
        to_string(_v_name)

.. py:method:: Portal.functions.isPrisoned(operatorId: uint256)

    ``True`` if the operator of given id has prisoned, ``False`` otherwise.

    .. code-block:: python

        portal.functions.isPrisoned(operatorId).call()
        # False

.. py:method:: Portal.functions.isPriceValid(poolId: uint256)

    ``True`` if the pool of given id has valid price, ``False`` otherwise.

    .. code-block:: python

        portal.functions.isPriceValid(poolId).call()
        # True

.. py:method:: Portal.functions.isMintingAllowed(poolId: uint256)

    ``True`` if the pool of given id allows minting, ``False`` otherwise.

    .. code-block:: python

        portal.functions.isMintingAllowed(poolId).call()
        # True

.. py:method:: Portal.functions.isPrivatePool(poolId: uint256)

    ``True`` if the pool of given id is private pool, ``False`` otherwise.

.. py:method:: Portal.functions.isWhitelisted(poolId: uint256, account: address)

    | ``True`` if the given address is whitelisted in given private pool.
    | ``False`` if not whitelised or if the pool is public.


.. py:method:: Portal.functions.getInfrastructureFee(_type : uint256)

    ``infrastructureFee`` as a percentage with respect to PERCENTAGE_DENOMINATOR for given package type.

.. py:method:: Portal.functions.getMaintenanceFee(id: uint256)

    ``MaintainanceFee`` as a percentage with respect to PERCENTAGE_DENOMINATOR. ``id`` can be operator or pool.

    .. code-block:: python

        portal.functions.getMaintenanceFee(operatorId).call()
        # 500000000
        # 500000000 / 1e10 = 0.05 %
        
.. py:method:: Portal.functions.getValidator(pubkey: bytes)

    Returns the ``Validator`` by given pubkey.

    * state
    * index
    * createdAt
    * period
    * poolId
    * operatorId
    * poolFee
    * operatorFee
    * infrastructureFee
    * signature31

    .. code-block:: python

        # Optionally both hexstring or bytes works.
        # Hex-string 
        pubkey = 0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d
        # Hex-to-bytes
        bytes.fromhex('9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d')
        # b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'
        
        # Bytes
        pubkey =  b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'
        # Bytes-to-hex
        pubkey.hex()
        # 0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d

        portal.functions.getValidator(pubkey).call()

.. py:method:: Portal.functions.getValidatorByPool(poolID: uint256, index: uint256)

    Returns the ``Validator`` of pool that corresponding index:

    * state
    * index
    * createdAt
    * period
    * poolId
    * operatorId
    * poolFee
    * operatorFee
    * infrastructureFee
    * signature31

    .. code-block:: python

        # Optionally both hexstring or bytes works.
        # Hex-string 
        pubkey = 0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d
        # Hex-to-bytes
        bytes.fromhex('9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d')
        # b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'

        # Bytes
        pubkey =  b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'
        # Bytes-to-hex
        pubkey.hex()
        # 0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d

        portal.functions.getValidatorByPool(poolId, 1).call()