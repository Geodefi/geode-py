.. _token:

============
Token (gETH)
============

.. py:module:: Token
.. py:currentmodule:: Token

.. py:class:: geodefi.Token


| One of the core components of Geodefi is the ERC1155 token, which allows for the creation and management of multiple fungible and non-fungible tokens on a single contract.
| One such token is gETH, which is a representation of Ether (ETH) that can be traded and transferred within the Geodefi ecosystem.
| ``Token`` object is created with respect to the provided API's chainId.

.. code-block:: python

    # will refer to Token instance of initiated Geode instance, as gETH.
    gETH = geode.token 

.. contents:: :local:
    
----------------
Class Attributes
----------------
    .. py:attribute:: Portal.address

        Returns the ``address`` of the contract.

    .. code-block:: python

        gETH.address
        # 0xB0334F08dEC465Ec180F1AF04C6D7d3737407083
        
    .. py:attribute:: Portal.network

        Returns the ``network`` of the contract as a ``geodefi.Network`` (strEnum) instance.

    .. code-block:: python

        gETH.network
        # <Network.holesky: 17000>    

---- 

---------
Functions
---------

ERC1155 Standarts
-----------------

.. py:method:: Token.functions.name(None)

    Returns the ``name`` of chain specific token.

.. code-block:: python

    gETH.functions.name().call()
    # 'Geode Staked Ether'

.. py:method:: Token.functions.mint(to, id, amount, data)

    "Creates `amount` new tokens for `to`, of token type `id`.
    
    * See {ERC1155-_mint}. Requirements: - the caller must have the `MINTER_ROLE`."

.. WARNING::

    The ``minting`` can already be done on ``Portal``.

.. code-block:: python

    gETH.functions.mint('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',5,1000000000000000000,'').buildTransaction(**config)


.. py:method:: Token.functions.mintBatch(to, id[], amount[], data)
    
    "Creates `amount` new tokens for `to`, of token type `id`. Enables multiple tokens with specific amounts.

.. code-block:: python
    
    # address,uint256[],uint256[],bytes
    gETH.functions.mintBatch('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',[5,12431254],[1000000000000000000,500000000000000000]'').buildTransaction(**config)
    
     
.. py:method:: Token.functions.balance(account, id)

    * ``account`` cannot be the zero address.

    Returns the ``balance`` of gETH token with ``id`` of the given ``account``.

.. code-block:: python

    # address,uint256
    gETH.functions.balance('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',5).call()
    # 1000000000000000000

.. py:method:: Token.functions.balanceOfBatch(accounts[], ids[])

    Batch version of above function. Inputs are list, outputs are list.
    * address[],uint256[]
    * `accounts` and `ids` must have the same length."

.. py:method:: Token.functions.denominator()

    Returns the ``denominator`` of gETH token. (1e18)

.. code-block:: python

    # 1e18
    gETH.functions.denominator().call()
    # 1000000000000000000

.. py:method:: Token.functions.symbol()

    Returns the ``symbol`` of gETH token. (1e18)

.. code-block:: python

    gETH.functions.symbol().call()
    #  'gETH'

.. py:method:: Token.functions.totalSupply(uint256 poolID)

    Returns the ``totalSupply`` integer of the given Pool Id.

.. code-block:: python

    # Check Pools page to see how to get pool ID.
    poolID = 50016835115526216130031110555486827201953559012021267556883950029143900999178
    gETH.functions.totalSupply(poolID).call()
    # 32000000000000000000

.. py:method:: Token.functions.burn(account, id, value)

    * ``account`` cannot be the zero address.

    Burns the ``value`` of gETH token with ``id`` of the given ``account``.

.. code-block:: python

    # address,uint256
    gETH.functions.burn('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',5, 1e18).buildTransaction()
    

.. py:method:: Token.functions.burnBatch(accounts, ids[], values[])

    Batch version of above function. Inputs are list, outputs are list.
    * address[],uint256[]
    * `accounts` and `ids` must have the same length."


.. py:method:: Token.functions.safeTransferFrom(address from, address to, uint256 id, uint256 amount, bytes memory data)

    * ``account`` cannot be the zero address.

    Burns the ``value`` of gETH token with ``id`` of the given ``account``.

.. code-block:: python

    # address,uint256
    gETH.functions.safeTransferFrom(addr1, addr2, id, 1e18, '').buildTransaction()
    

.. py:method:: Token.functions.safeBatchTransferFrom(address to, ids[], amount[], '')

    * amounts: uint256[], ids: uint256[]
    * `amounts` and `ids` must have the same length."

    Batch version of above function. Inputs are list, outputs are list.

---- 

Middlewares 
------------

The ``ERC1155`` standard can host multiple tokens and ensures that the entire system works in the ERC1155 standard. 
Depending on the structure, users can set ``middleware`` to certain tokens in line and make it functions as ``ERC20``.

.. py:method:: Token.functions.isMiddleware(address middleware, uint256 id)

    Check if an address is approved as an middleware for an ID

.. code-block:: python

    gETH.functions.isMiddleware('0xaa..', 3).call()
    # True

.. py:method:: Token.functions.setMiddleware(address middleware, uint256 id, bool isSet)

    Set an address of a contract that will act as a middleware on gETH contract for a specific ID

.. code-block:: python

    gETH.functions.setMiddleware('0xaa..', 3, True).buildTransaction()
        
---- 

Avoiders 
---------

    Users can avoid the effect of the ``middleware`` functionalities.

.. py:method:: Token.functions.isAvoider(address account, uint256 id)

    Checks if the given address restricts the affect of the middlewares on their gToken

    .. code-block:: python

        gETH.functions.isAvoider('0xaa..', 3).call()
        # True

.. py:method:: Token.functions.avoidMiddlewares(uint256 id, bool isAvoid)

    Restrict any affect of middlewares on the tokens of caller

    ``isAvoid`` - ``true`` restrict middlewares, ``false``: allow middlewares

    .. code-block:: python

        gETH.functions.avoidMiddlewares(3, True).buildTransaction()

---- 

PricePerShare
--------------

.. py:method:: Token.functions.pricePerShare(uint256 poolID)

    Returns the ``pricePerShare`` of the given Pool Id.

    * The denominator is 1e18 by default. Therefore, 1e18 indicates 1:1 ratio with ETH.

    .. code-block:: python

        # Check Pools page to see how to get pool ID.
        poolID = 50016835115526216130031110555486827201953559012021267556883950029143900999178
        gETH.functions.pricePerShare(poolID).call()
        # 1000000000000000000

.. py:method:: Token.functions.setPricePerShare(price: uint256, id: uint256)

    Change the ``pricePerShare`` variable for given ``id``.

    .. code-block:: python

        # Check Pools page to see how to get pool ID.
        poolID = 50016835115526216130031110555486827201953559012021267556883950029143900999178
        gETH.functions.setPricePerShare(1, poolID).buildTransaction()
        

.. py:method:: Token.functions.priceUpdateTimestamp(poolID: uint256)

    Get the last timestamp of ``priceUpdate`` that occured in given pool ID.


    .. code-block:: python

        # Given pool ID
        gETH.functions.priceUpdateTimestamp(poolID).call()
        # 1677379164

---- 

Roles 
-----

.. py:method:: Token.functions.DEFAULT_ADMIN_ROLE()

    Returns the ``DEFAULT_ADMIN_ROLE`` of gETH token. Only this address have permission to run admin functions.
    For details check docs.geode.fi.

    .. code-block:: python

        # bytes32
        gETH.functions.DEFAULT_ADMIN_ROLE().call()
        # 'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
        # hex-string
        gETH.functions.DEFAULT_ADMIN_ROLE().call().hex()
        # '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.functions.PAUSER_ROLE()

    Returns the ``PAUSER_ROLE`` of gETH token. Only this address have permission to run pause/unpause functions.
    For details check docs.geode.fi.

    .. code-block:: python

        # bytes32
        gETH.functions.PAUSER_ROLE().call()
        # 'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
        # hex-string
        gETH.functions.PAUSER_ROLE().call().hex()
        # '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.functions.MINTER_ROLE()

    Returns the ``MINTER_ROLE`` of gETH token. Only this address have permission to run mint functions.
    For details check docs.geode.fi.

    .. code-block:: python

        # bytes32
        gETH.functions.MINTER_ROLE().call()
        # 'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
        # hex-string
        gETH.functions.MINTER_ROLE().call().hex()
        # '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.functions.ORACLE_ROLE()

    Returns the ``ORACLE_ROLE`` of gETH token. Only this address have permission to run oracle functions.
    For details check docs.geode.fi.

    .. code-block:: python

        # bytes32
        gETH.functions.ORACLE_ROLE().call()
        # 'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
        # hex-string
        gETH.functions.ORACLE_ROLE().call().hex()
        # '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.functions.MIDDLEWARE_MANAGER_ROLE()

    Returns the ``MIDDLEWARE_MANAGER_ROLE`` of gETH token. Only this address have permission to run middleware functions.
    For details check docs.geode.fi.

    * See the Middlewares section below.

    .. code-block:: python

        # bytes32
        gETH.functions.MIDDLEWARE_MANAGER_ROLE().call()
        # 'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
        # hex-string
        gETH.functions.MIDDLEWARE_MANAGER_ROLE().call().hex()
        # '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.functions.URI_SETTER_ROLE()

    Returns the ``URI_SETTER_ROLE`` of gETH token. Only this address have permission to set URIs to access ipfs data in ERC1155.
    For details check docs.geode.fi.

    .. code-block:: python

        # bytes32
        gETH.functions.URI_SETTER_ROLE().call()
        # 'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
        # hex-string
        gETH.functions.URI_SETTER_ROLE().call().hex()
        # '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.functions.transferMinterRole(address new_minter_address)

    Changes the ``MINTER_ROLE`` of gETH token.

    .. code-block:: python

        gETH.functions.transferMinterRole(newMinter).buildTransaction()

.. py:method:: Token.functions.transferOracleRole(address new_address)

    Changes the ``ORACLE_ROLE`` of gETH token.

    .. code-block:: python

        gETH.functions.transferOracleRole(newOracle).buildTransaction()

.. py:method:: Token.functions.transferPauserRole(address new_address)

    Changes the ``PAUSER_ROLE`` of gETH token.

    .. code-block:: python

        gETH.functions.transferPauserRole(address newPauser).buildTransaction()

.. py:method:: Token.functions.transferMiddlewareManagerRole(address new_address)

    Changes the ``MIDDLEWARE_MANAGER_ROLE`` of gETH token.

    .. code-block:: python

        gETH.functions.transferMiddlewareManagerRole(address newMiddlewareManager).buildTransaction()

.. py:method:: Token.functions.transferUriSetterRole(address newURISetter)

    Changes the ``URI_SETTER_ROLE`` of gETH token.

    .. code-block:: python

        gETH.functions.transferUriSetterRole(newURISetter).buildTransaction()

---- 

Pausing 
-------

.. py:method:: Token.functions.paused

    Gets bool variable whether contract has paused or not.

.. code-block:: python

    gETH.functions.paused().call()

.. py:method:: Token.functions.pause()

    Pauses all token transfers and approvals.

.. code-block:: python

    gETH.functions.pause().buildTransaction()

.. py:method:: Token.functions.unpause()

    Unpauses all token transfers and approvals.

.. code-block:: python

    gETH.functions.unpause().buildTransaction()