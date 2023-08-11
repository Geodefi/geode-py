.. _quickstart:

Quickstart
===========

.. NOTE:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Before Starting
----------------

.. WARNING::
  Geodefi v1.1.1 only supports the python versions between 3.7 and 3.10.  

Installation
-------------

Geodefi can be installed (preferably in a virtualenv )
using ``pip`` as follows:


.. code-block:: shell
  
   >>> python3 -m venv venv
   >>> source venv/bin/activate  
   >>> pip install geodefi



Using Geodefi
---------------

Geodefi is a Python library that leverages the power of web3.py, offering developers a comprehensive toolkit for Geode Finance interactions. Before using, we recommend that you read the `documentation <https://docs.geode.fi>`_ to become familiar with the terms.

Initialize Geode
********************

Check out :ref:`Initializing Geode <_initializing_geode>`

Get Started with Staking Pools
********************************

.. note::

  In some examples, the ``id`` s of the roles are necessary to get information. 
  You can learn the ``id`` s of the relevant ``pool``, ``operator`` or ``validator`` 
  from the our `website <https://www.geode.fi>`_ or from the :ref:`Initializing Geode <_initializing_geode>` documentation.

Since Geodefi is built on top of web3.py you can get most of the information just like in web3.py.

.. code-block:: python

   ## Pool Info
   >>> pid = 50016835115526216130031110555486827201953559012021267556883950029143900999178
   >>> myPool = GEODE.Portal.pool(pid)
   >>> print("NAME:",myPool.NAME)
    NAME: Ice Bear's Pool
   >>> print("CONTROLLER:",myPool.CONTROLLER)
    CONTROLLER: 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C

   ## View functions
   >>> myPortal = GEODE.Portal
   >>> myPortal.functions.getContractVersion().call()
    87373968589722757255522487689903791119558634447171488905970002736659167479131


   >>> _id = 29228457249232120346521013786824808088246537603535847808963148138747123868265
   >>> myPortal.functions.getKey(_id,toBytes32('surplus')).call()
    b'\x96\xbe\\\xf8\xab\x14\x94q\x7f(V>\x19\xcd{\xe8\xf6\x7f\xedP"\xc1\x91nW<\x04\xb9>C<\xe3'
   
   ## gETH
   >>> GEODE.gETH.contract.functions.priceUpdateTimestamp(pid).call()
    1677379164

Sending Transactions
*****************************

Roles such as ``SENATE``, ``GOVERNANCE``, ``maintainer`` have been produced for most functions in the Geode Ecosystem. 
Some critical functions can only be called by such roles.


.. NOTE::
  To call transact functions, you need to have private_key of corresponding ethereum address.
  Please store your private_key safely.


1. Get Private Key

.. code-block:: python

  >>> private_key = os.environ["PRIV_KEY"]

2. Create account on Geode's web3py instance

.. code-block:: python

  >>> myAccount = G.w3.eth.account.from_key(private_key)


3. Allow Geodefi to use your private key in your local

.. code-block:: python

  >>> from web3.middleware import construct_sign_and_send_raw_middleware
  >>> G.w3.middleware_onion.add(construct_sign_and_send_raw_middleware(myAccount))

4. Set default account if one address is used generally

.. code-block:: python

  >>> G.w3.eth.defaultAccount = myAccount

5. Transact

.. code-block:: python

  ## Sample transact
  >>> Portal.functions.increaseWalletBalance(myOperator.ID).transact({"from": myAccount.address, "value":3e18})


.. note::

  Geodefi's property functions are not expensive because they return local variables. 
  These variables are automatically updated every 60 (``REFRESH_RATE``) seconds.


