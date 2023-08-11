.. _portal:


Portal
============

.. contents:: :local:

.. py:module:: portal
.. py:currentmodule:: portal


.. py:class:: Geode.Portal()

The ``portal`` package houses public utility functions from Portal contract.

.. WARNING:: 
    You may want to make sure to double-check the gas limit when executing transactions to prevent potential out-of-gas errors and unexpected transaction failures.


Attributes
------------

.. py:attribute:: Portal.address

    Returns the ``address`` of the contract.

.. code-block:: python

    # get a Portal address
    >>> geode.Portal.address
     0xB0334F08dEC465Ec180F1AF04C6D7d3737407083
    
    >>> PORTAL = geode.Portal

.. py:attribute:: Portal.version

    Returns the ``version`` of the contract.

.. code-block:: python

    # get a Portal address
    >>> geode.Portal.version
      87373968589722757255522487689903791119558634447171488905970002736659167479131    

.. py:attribute:: Portal.network

    Returns the ``network`` of the contract.

.. code-block:: python

    # get a Portal address
    >>> geode.Portal.network
      <Network.goerli: 5>    


Methods
------------

.. py:method:: Portal.functions.GeodeParams()

    Returns: 
        * ``governance``
        * ``senate``
        * ``approvedUpgrade`` 
        * ``senateExpiry`` 
        * ``packageType`` 

.. code-block:: python

    # get a Portal address
    >>> Portal.functions.GeodeParams().call()
    ['0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
    '0x6699580E23Fc6a802e996a654845348CA560bc94',
    1717847448,
    10001]


.. py:method:: Portal.functions.StakeParams()

    Returns:
        * ``gETH``
        * ``oraclePosition``
        * ``validatorsIndex``
        * ``verificationIndex``
        * ``monopolyThreshold``
        * ``oracleUpdateTimestamp``
        * ``dailyPriceIncreaseLimit``
        * ``dailyPriceDecreaseLimit``
        * ``governanceFee``
        * ``priceMerkleRoot``
        * ``balanceMerkleRoot``

.. code-block:: python

    # get a Portal address
    >>> Portal.functions.StakeParams().call()
    ['0x3f911696044d000CcF7D085e35b060e846b95f56',
    '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C',
    0,
    0,
    500000,
    0,
    700000000,
    700000000,
    0,
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']


.. py:method:: Portal.functions.getContractVersion()

    Returns ``version`` of contract in integer.


.. code-block:: python

    # get a Portal address
    >>> Portal.functions.getContractVersion().call()
    87373968589722757255522487689903791119558634447171488905970002736659167479131


Portal: Reading Isolated Storage
-----------------------------------

.. NOTE:: 
    Please read the `Isolated Storage <https://docs.geode.fi/key-concepts/portal/isolated-storage>`_ in Geode Finance Docs.

.. WARNING::
    We recommend that you initialize the ``Pool``, ``Operator`` or ``Validator`` and read the data that way, instead of calling it from the ``Portal`` contract. 
    See :doc:`Pools <pool>`, :doc:`Operators <operator>`, :doc:`Validators <validator>`,

.. py:method:: Portal.functions.readBytes(uint256, bytes32)

.. code-block:: python

    >>> from geode.utils import toBytes32, toString
    >>> pid = 29228457249232120346521013786824808088246537603535847808963148138747123868265
    >>> Portal.functions.readBytes(pid, toBytes32("NAME")).call()
      b'Icy Pool'
    >>> toString(b'Icy Pool')
       'Icy Pool'

.. py:method:: Portal.functions.readAddress(uint256, bytes32)

.. code-block:: python

    >>> from geode.utils import toBytes32
    >>> pid = 29228457249232120346521013786824808088246537603535847808963148138747123868265
    >>> Portal.functions.readAddress(pid, toBytes32("CONTROLLER")).call()
      '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'


.. py:method:: Portal.functions.readUint(uint256, bytes32)

.. code-block:: python

    >>> from geode.utils import toBytes32
    >>> pid = 29228457249232120346521013786824808088246537603535847808963148138747123868265
    >>> Portal.functions.readUint(pid, toBytes32("fee")).call()
      500000000


.. NOTE::
    Do not forget to call the correct function according to the type of the variable you will return.

Reading Arrays
*****************

.. NOTE::
    If you want to get lenght of the array you can call ``readUint`` function with the same keyword like below function.


.. code-block:: python

    >>> Portal.functions.readAddressArray(pid, toBytes32("middlewares")).call()
    ['0x..','0x..','0x..']

    >>> Portal.functions.readUint(pid, toBytes32("middlewares")).call()
    3


.. py:method:: Portal.functions.readBytesArray(uint256, bytes32)

For getting array of ``bytes``.

.. py:method:: Portal.functions.readAddressArray(uint256, bytes32)

For getting array of ``address``.

.. py:method:: Portal.functions.readUintArray(uint256, bytes32)

For getting array of ``uint256``.


Getting IDs from Portal's Storage
-----------------------------------

.. py:method:: Portal.functions.allIdsByType(type: uint256, index: uint256)

    Returns the ``id`` of specific type of given index.
    
.. code-block:: python

    >>> from geode.globals import ID_TYPE

    # Get Pools (ID_TYPE => 5)
    >>> Portal.functions.allIdsByType(ID_TYPE.POOL,0).call()
      29228457249232120346521013786824808088246537603535847808963148138747123868265
    >>> Portal.functions.allIdsByType(5,1).call()
      50016835115526216130031110555486827201953559012021267556883950029143900999178
    >>> Portal.functions.allIdsByType(ID_TYPE.POOL,99).call()
      ContractLogicError

    # Get Operators (ID_TYPE => 4)
    >>> Portal.functions.allIdsByType(ID_TYPE.OPERATOR,0).call()
      114391297015478800753082638170652680401082080549997516459063441314156612391510
    >>> Portal.functions.allIdsByType(4,1).call()
      51559110727159830236523264446237638129364818047104669081802875007477059353434


.. py:method:: Portal.functions.allIdsByTypeLength(type: uint256)

    Returns the ``lenght`` of specific type of given index.
    
.. code-block:: python

    >>> from geode.globals import ID_TYPE

    # Get Pools Length (ID_TYPE => 5)
    >>> Portal.functions.allIdsByTypeLength(ID_TYPE.POOL).call()
      13

    # Get Operators Length (ID_TYPE => 4)
    >>> Portal.functions.allIdsByTypeLength(ID_TYPE.OPERATOR).call()
      5


How IDs Are generated
---------------------------


.. py:method:: Portal.functions.generateId(name: string, type: uint256)

    It returns keccak256 hash of encoded name and type.

.. code-block:: python

    >>> Portal.functions.generateId(b'Some_Pool', 5).call()
      97770474815149397909782741678802560703260876453812799861980400297568557242506

.. py:method:: Portal.functions.getKey(id: uint256, param: bytes32)

    Each variable of roles stores in mappings. To optimize storage, each key directs the specific parameter with given id in mapping.

.. code-block:: python

    >>> from geode.utils import toBytes32

    # Bytes
    >>> Portal.functions.getKey(poolID, toBytes32('CONTROLLER')).call()
      b'\xb4s\xca\xe0\xf2\xd9\xf2!*k\xfd$\xd9\xff\xcc\n\xf8\xcc7>\xae{=\x8f&\xb9\xbe\xc6_\x00^\xdf'



Get Validator Data from Portal
-----------------------------------

.. py:method:: Portal.functions.getValidator(pubkey: bytes)

    Returns the ``Validator`` by given pubkey.

.. code-block:: python

    ### Optionally both hexstring or bytes works.
    ## Hex-string 
    >>> pubkey = 0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d
    ## Hex-to-bytes
    >>> bytes.fromhex('9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d')
      b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'
      
    ## Bytes
    >>> pubkey =  b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'
    ## Bytes-to-hex
    >>> pubkey.hex()
      0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d

    >>> Portal.functions.getValidator(pubkey).call()
        (2,
        1,
        50016835115526216130031110555486827201953559012021267556883950029143900999178,
        114391297015478800753082638170652680401082080549997516459063441314156612391510,
        500000000,
        500000000,
        0,
        1677383052,
        1692935052,
        b'\x94\xc0\x18~I\x0e\xc3\x96r&\xd3\xc3\xce\xbc\xf0\xb0t\xbf\xa0Iq\xe5+\x95t\x8e\x91\x93?\x93\xfc?\x93g}\x94tM\xf5 \x89|\x99\xd3sn\xd1\xdb\x08\xa8!i\x813\xc2b\xb3SdB\x95Y\xa1\xb0z\xc4\x85`\xd2z.g\x88Dq\xf8R/g\xae\nB\xfa\xaa\xee!~\x9c@\xe0\\\xd91(\xad\xdb')


.. py:method:: Portal.functions.getValidatorByPool(poolID: uint256, index: uint256)

    Returns the ``Validator`` of pool that corresponding index.

.. code-block:: python

    >>> Portal.functions.getValidatorByPool(poolID, 0).call()
        (2,
        1,
        50016835115526216130031110555486827201953559012021267556883950029143900999178,
        114391297015478800753082638170652680401082080549997516459063441314156612391510,
        500000000,
        500000000,
        0,
        1677383052,
        1692935052,
        b'\x94\xc0\x18~I\x0e\xc3\x96r&\xd3\xc3\xce\xbc\xf0\xb0t\xbf\xa0Iq\xe5+\x95t\x8e\x91\x93?\x93\xfc?\x93g}\x94tM\xf5 \x89|\x99\xd3sn\xd1\xdb\x08\xa8!i\x813\xc2b\xb3SdB\x95Y\xa1\xb0z\xc4\x85`\xd2z.g\x88Dq\xf8R/g\xae\nB\xfa\xaa\xee!~\x9c@\xe0\\\xd91(\xad\xdb')


.. WARNING::
    The offchain version of below functions have already implemented. Optionally: Use built-in functions in geode.utils.


Additional View Functions for Pools, Operators and Validators
---------------------------------------------------------------
.. py:method:: Portal.functions.isPrisoned(operatorId: uint256)

    ``True`` if the operator of given id has prisoned, ``False`` otherwise.


.. code-block:: python

    ## operatorId: uint256
    >>> Portal.functions.isPrisoned(operatorId).call()
      False


.. py:method:: Portal.functions.isPrivatePool(poolId: uint256)

    ``True`` if the pool of given id is private pool, ``False`` otherwise.

.. code-block:: python

    ## poolID: uint256
    >>> Portal.functions.isPrivatePool(poolId).call()
      False


.. py:method:: Portal.functions.isPriceValid(poolId: uint256)

    ``True`` if the pool of given id has valid price, ``False`` otherwise.

.. code-block:: python

    ## poolID: uint256
    >>> Portal.functions.isPriceValid(poolId).call()
      True

.. py:method:: Portal.functions.isMintingAllowed(poolId: uint256)

    ``True`` if the pool of given id allows minting, ``False`` otherwise.

.. code-block:: python

    ## poolID: uint256
    >>> Portal.functions.isMintingAllowed(poolId).call()
      True

.. py:method:: Portal.functions.canStake(pubkey: uint256)

    ``True`` if the validator of given pubkey passed the checks and is ready to stake, ``False`` otherwise.

.. code-block:: python

    ## pubkey: bytes
    >>> Portal.functions.canStake(pubkey).call()
      True

.. py:method:: Portal.functions.getMaintenanceFee(operatorId: uint256)

    ``MaintainanceFee`` 1e10 means 10% of commision will be payed to operator.

.. code-block:: python

    ## operatorId: uint256
    >>> Portal.functions.getMaintenanceFee(operatorId).call()
      500000000
    >>> 500000000 / 1e10 
      0.05


