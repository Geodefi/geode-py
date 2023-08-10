.. _geth:


gETH
===========

# TODO warning message

One of the core components of Geode Finance is the ERC1155 token, which allows for the creation and management of multiple fungible and non-fungible tokens on a single contract. One such token is gETH, which is a representation of Ether (ETH) that can be traded and transferred within the Geode Finance ecosystem. In this documentation, we will explore how to interact with the gETH token contract using Python and the Web3 library.

.. py:attribute:: Geode.Token

    Returns the ``Token`` object. 

.. code-block:: python

    # Initilize Geode
    >>> G = Geode(exec_api=env["EXECUTION_API"], cons_key= env["CONSENSUS_KEY"])
    # Initilize Token
    >>> gETH = G.Token


Basic Standarts
-----------------

.. py:method:: Token.contract.functions.name(None)

    Returns the ``name`` of gETH token.

.. code-block:: python

    >>> gETH.contract.functions.name().call()
    'Geode Staked Ether'


.. py:method:: Token.contract.functions.mint(to, id, amount, data)

    "Creates `amount` new tokens for `to`, of token type `id`.
    
    * See {ERC1155-_mint}. Requirements: - the caller must have the `MINTER_ROLE`."

.. code-block:: python

    >>> gETH.contract.functions.mint('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',5,1000000000000000000,'').buildTransaction(**config)


.. py:method:: Token.contract.functions.mintBatch(to, id[], amount[], data)
    
    "Creates `amount` new tokens for `to`, of token type `id`. Enables multiple tokens with specific amounts.

.. code-block:: python
    
    # address,uint256[],uint256[],bytes
    >>> gETH.contract.functions.mintBatch('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',[5,12431254],[1000000000000000000,500000000000000000]'').buildTransaction(**config)
    
     
.. py:method:: Token.contract.functions.balance(account, id)

    * ``account`` cannot be the zero address.

    Returns the ``balance`` of gETH token with ``id`` of the given ``account``.

.. code-block:: python

    # address,uint256
    >>> gETH.contract.functions.balance('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',5).call()
    1000000000000000000

.. py:method:: Token.contract.functions.balanceOfBatch(accounts[], ids[])

    Batch version of above function. Inputs are list, outputs are list.
    * address[],uint256[]
    * `accounts` and `ids` must have the same length."

.. py:method:: Token.contract.functions.denominator()

    Returns the ``denominator`` of gETH token. (1e18)

.. code-block:: python

    # 1e18
    >>> gETH.contract.functions.denominator().call()
    1000000000000000000

.. py:method:: Token.contract.functions.symbol()

    Returns the ``symbol`` of gETH token. (1e18)

.. code-block:: python

    >>> gETH.contract.functions.symbol().call()
    'gETH'

.. py:method:: Token.contract.functions.totalSupply(uint256 poolID)

    Returns the ``totalSupply`` integer of the given Pool Id.

.. code-block:: python

    # Check Pools page to see how to get pool ID.
    >>> poolID = 50016835115526216130031110555486827201953559012021267556883950029143900999178
    >>> gETH.contract.functions.totalSupply(poolID).call()
    32000000000000000000

.. py:method:: Token.contract.functions.pricePerShare(uint256 poolID)

    Returns the ``pricePerShare`` of the given Pool Id.

    * The denominator is 1e18 by default. Therefore, 1e18 indicates 1:1 ratio with ETH.

.. code-block:: python

    # Check Pools page to see how to get pool ID.
    >>> poolID = 50016835115526216130031110555486827201953559012021267556883950029143900999178
    >>> gETH.contract.functions.pricePerShare(poolID).call()
    1000000000000000000

.. py:method:: Token.contract.functions.setPricePerShare(price: uint256, id: uint256)

    Change the ``pricePerShare`` variable for given ``id``.

.. code-block:: python

    # Check Pools page to see how to get pool ID.
    >>> poolID = 50016835115526216130031110555486827201953559012021267556883950029143900999178
    >>> gETH.contract.functions.setPricePerShare(1, poolID).buildTransaction()
    

.. py:method:: Token.contract.functions.burn(account, id, value)

    * ``account`` cannot be the zero address.

    Burns the ``value`` of gETH token with ``id`` of the given ``account``.


.. code-block:: python

    # address,uint256
    >>> gETH.contract.functions.burn('0xd3CdA913deB6f67967B99D67aCDFa1712C293601',5, 1e18).buildTransaction()
    

.. py:method:: Token.contract.functions.burnBatch(accounts, ids[], values[])

    Batch version of above function. Inputs are list, outputs are list.
    * address[],uint256[]
    * `accounts` and `ids` must have the same length."


.. py:method:: Token.contract.functions.safeTransferFrom(address from, address to, uint256 id, uint256 amount, bytes memory data)

    * ``account`` cannot be the zero address.

    Burns the ``value`` of gETH token with ``id`` of the given ``account``.


.. code-block:: python

    # address,uint256
    >>> gETH.contract.functions.safeTransferFrom(addr1, addr2, id, 1e18, '').buildTransaction()
    

.. py:method:: Token.contract.functions.safeBatchTransferFrom(address to, ids[], amount[], '')

    * amounts: uint256[], ids: uint256[]
    * `amounts` and `ids` must have the same length."
    Batch version of above function. Inputs are list, outputs are list.


.. py:method:: Token.contract.functions.priceUpdateTimestamp(poolID: uint256)

    Get the last timestamp of ``priceUpdate`` that occured in given pool ID.


.. code-block:: python

    # Given pool ID
    >>> gETH.contract.functions.priceUpdateTimestamp(poolID).call()
     1677379164



 '',


Roles 
--------

.. py:method:: Token.contract.functions.DEFAULT_ADMIN_ROLE()

    Returns the ``DEFAULT_ADMIN_ROLE`` of gETH token. Only this address have permission to run admin functions.
    For details check docs.geode.fi.

.. code-block:: python

    # bytes32
    >>> gETH.contract.functions.DEFAULT_ADMIN_ROLE().call()
    'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
    # hex-string
    >>> gETH.contract.functions.DEFAULT_ADMIN_ROLE().call().hex()
    '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.contract.functions.PAUSER_ROLE()

    Returns the ``PAUSER_ROLE`` of gETH token. Only this address have permission to run pause/unpause functions.
    For details check docs.geode.fi.

.. code-block:: python

    # bytes32
    >>> gETH.contract.functions.PAUSER_ROLE().call()
    'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
    # hex-string
    >>> gETH.contract.functions.PAUSER_ROLE().call().hex()
    '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.contract.functions.MINTER_ROLE()

    Returns the ``MINTER_ROLE`` of gETH token. Only this address have permission to run mint functions.
    For details check docs.geode.fi.

.. code-block:: python

    # bytes32
    >>> gETH.contract.functions.MINTER_ROLE().call()
    'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
    # hex-string
    >>> gETH.contract.functions.MINTER_ROLE().call().hex()
    '0000000000000000000000000000000000000000000000000000000000000000'

.. py:method:: Token.contract.functions.ORACLE_ROLE()

    Returns the ``ORACLE_ROLE`` of gETH token. Only this address have permission to run oracle functions.
    For details check docs.geode.fi.

.. code-block:: python

    # bytes32
    >>> gETH.contract.functions.ORACLE_ROLE().call()
    'b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00''
    # hex-string
    >>> gETH.contract.functions.ORACLE_ROLE().call().hex()
    '0000000000000000000000000000000000000000000000000000000000000000'


.. py:method:: Token.contract.functions.updateMinterRole(address new_minter_address)

    Changes the ``MINTER_ROLE`` of gETH token.

.. code-block:: python

    >>> gETH.contract.functions.updateMinterRole(newMinter).buildTransaction()

.. py:method:: Token.contract.functions.updateOracleRole(address new_address)

    Changes the ``ORACLE_ROLE`` of gETH token.

.. code-block:: python

    >>> gETH.contract.functions.updateOracleRole(newOracle).buildTransaction()

.. py:method:: Token.contract.functions.updatePauseRole(address new_address)

    Changes the ``PAUSER_ROLE`` of gETH token.

.. code-block:: python

    >>> gETH.contract.functions.updatePauserRole(newPause).buildTransaction()



Middlewares 
--------
  'setMiddleware',
  'avoidMiddlewares',

Pauses 
-------

.. py:method:: Token.contract.functions.pause()

    Pauses all token transfers and approvals.

.. code-block:: python

    >>> gETH.contract.functions.pause().buildTransaction()

.. py:method:: Token.contract.functions.paused()

    Gets bool variable whether contract has paused or not.

.. code-block:: python

    >>> gETH.contract.functions.paused().call()

.. py:method:: Token.contract.functions.unpause()

    Unpauses all token transfers and approvals.

.. code-block:: python

    >>> gETH.contract.functions.unpause().buildTransaction()


Checks 
---------


 'exists',

 'isApprovedForAll',
 'isAvoider',
 'isMiddleware',






