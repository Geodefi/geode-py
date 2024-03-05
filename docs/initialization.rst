.. _initialization:

=============================
Initialization & Introduction
=============================

---------------------------
Initialize Geode Object
---------------------------

.. code-block:: python

  # Get keys from enviroment
  import os
  EXECUTION_API = os.environ['EXECUTION_API']
  CONSENSUS_API = os.environ['CONSENSUS_API']

  # Initilize Geode
  from geodefi import Geode
  geode = Geode(exec_api = EXECUTION_API, cons_api = CONSENSUS_API,)

  #  INFO : Connected to beconchain
  #  INFO : Token:gETH
  #  INFO : Portal:holesky head is on 'v1_0'

Note that, we did not utilize ``PRIVATE_KEY`` from environment variables. You will need to take extra steps to make it possible.

----

-----------------
Send Transactions 
-----------------

Setting up your wallet with PRIVATE_KEY
---------------------------------------

.. code-block:: python

  from web3.middleware import construct_sign_and_send_raw_middleware
  private_key = os.environ["PRIVATE_KEY"] # name it to something else!!!

  # Create account on Geode's web3py instance
  acct = geode.w3.eth.account.from_key(private_key)

  # Allow Geodefi to use your private key
  geode.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(acct))

  # Set default account if one address is used generally
  geode.w3.eth.defaultAccount = acct


Sending transactions with .transact()
-------------------------------------

After connecting your wallet as a middleware onion, you can utilize ``.transact()`` to send transactions with apprepriote function calls. 

.. code-block:: python

  import math

  geode.portal.functions.increaseWalletBalance(myOperator.ID).transact({"from": acct.address, "value":math.floor(1e18)})

----

-----------------------
Customize Configuration
-----------------------

Configure the logger, or parameters such as  ``MAX_ATTEMPT``, ``ATTEMPT_RATE``, and ``REFRESH_RATE`` according to your use case and needs.

Example transaction:

.. code-block:: python

  # You can config the logging to get detailed outputs
  import logging
  logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(message)s')

  # api requests will fail after 10 calls.
  geode.MAX_ATTEMPT = 10 
  
  # interval between api requests (in seconds)
  geode.ATTEMPT_RATE = 0.1 
  
  # cached data will be refreshed after 60 seconds,
  # for 60 seconds there won't be any api calls to update the same data.
  # set to '0' to remove the cache, might cause excessive api usage.
  geode.REFRESH_RATE = 60  

----

-------------------------------------
Introduction to Bound Class Instances
-------------------------------------

Geode instances are chain agnostic, meaning any chain geodefi is deployed on is automatically connected when API endpoint is provided.
Geode instances provide access to the following sub-classes:

.. py:class:: geodefi.Geode.Portal
  
  Provides easy access to the main smart contract of the infrastructure: Portal.

  .. code-block:: python
  
    portal = geode.portal

  - Calling functions

    .. code-block:: python
      
      portal.functions.StakeParams().call()

  - Executing transactions

    .. code-block:: python

      portal.functions.increaseWalletBalance(myOperator.ID).transact({"from": acct.address, "value":math.floor(1e18)})

  - Deep Dive: :ref:`portal`

.. py:class:: geodefi.Geode.Token

  | Provides easy access to the internal accounting token of the provided chain.
  | These tokens are ``ERC1155`` tokens that keeps the balance of the staker with respect to pool id.  
  | For example ``gETH`` is the token that is available on Ethereum Blockchain.

  .. code-block:: python

    token = geode.token

    token.functions.balanceOf("0x7B6fA217a374826FCa50dccB87041AE0e34Ba1f5",30170521210884580269409068052100176225254765285183496335708525497309778819647).call()

  - Deep Dive: :ref:`token`

.. py:class:: geodefi.Geode.Beacon

  Allows user to query beaconchain data, with respect to the `provided api specification. <https://ethereum.github.io/beacon-APIs/?urls.primaryName=v2.4.0>`_

  .. code-block:: python

    beacon = geode.beacon

    beacon.beacon_genesis()

  - Deep Dive: :ref:`beacon`

.. py:class:: geodefi.Geode.Portal.Pool(uint256)

  By calling this function you can create a ``Pool`` class instance with the given ``ID``. 

  .. code-block:: python

    myPool = geode.portal.pool(50016835115526216130031110555486827201953559012021267556883950029143900999178)
    # INFO : ID TYPE:POOL:50016835115526216130031110555486827201953559012021267556883950029143900999178

  - Deep Dive: :ref:`pool`

.. py:class:: geodefi.Geode.Portal.Operator(uint256)

  By calling this function you can create a ``Operator`` class instance with the given ``ID``. 

  .. code-block:: python

    myOperator = geode.portal.operator(114391297015478800753082638170652680401082080549997516459063441314156612391510)
    # INFO : ID TYPE:OPERATOR:114391297015478800753082638170652680401082080549997516459063441314156612391510

  - Deep Dive: :ref:`operator`

.. py:class:: geodefi.Geode.Portal.Validator(bytes)

  By calling this function you can create a ``Validator`` class instance with the given ``pubkey``. 

  .. code-block:: python

    # string starting with 0x
    # OR 
    # bytes without 0x
    pubkey="0xb53e4800c249a97616a8f8aa56a749161b1ed06dca972547e79554230136d0704099c4c4b110e9b4fa278554587e6486" 
    myVal = geode.portal.validator(pubkey)
    # INFO : Connected to the validator: 0xb53e4800c249a97616a8f8aa56a749161b1ed06dca972547e79554230136d0704099c4c4b110e9b4fa278554587e6486
    
  - Deep Dive: :ref:`validator`
