.. _quickstart:

Quickstart
===========

.. NOTE:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Installation
------------

Geode-py can be installed (preferably in a :ref:`virtualenv <setup_environment>`)
using ``pip`` as follows:

.. code-block:: shell

   $ pip install geodefi

Using Geode-Py
---------------

Geode-Py is a Python library that leverages the power of web3.py, offering developers a comprehensive toolkit for Geode Finance interactions. Before using, we recommend that you read the `documentation <docs.geode.fi>`_ to become familiar with the terms.


Getting Geode Info
********************

.. note::

  In most examples, the ``id`` s of the roles are necessary to get information. 
  You can learn the ``id`` s of the relevant ``pool``, ``operator`` or ``validator`` 
  from the our `website <https://www.geode.fi>`_ or from the :ref:`Initilize-Geode<_initilize_geode>` documentation.

Since geode-py is built on top of web3.py you can get most of the information just like in web3.py.

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
   >>> myPortal.contract.functions.CONTRACT_VERSION().call()
    87373968589722757255522487689903791119558634447171488905970002736659167479131


   >>> _id = 29228457249232120346521013786824808088246537603535847808963148138747123868265
   >>> myPortal.contract.functions.getKey(_id,toBytes32('surplus')).call()
    b'\x96\xbe\\\xf8\xab\x14\x94q\x7f(V>\x19\xcd{\xe8\xf6\x7f\xedP"\xc1\x91nW<\x04\xb9>C<\xe3'
   
   ## gETH
   >>> GEODE.gETH.contract.functions.priceUpdateTimestamp(pid).call()
    1677379164

Interaction with Contracts
*****************************

Roles such as ``SENATE``, ``GOVERNANCE``, ``MAINTAINER`` have been produced for most functions in the Geode Ecosystem. 
Some critical functions can only be called by such roles.

.. code-block:: python

    ## Sample Public Key
   >>> sample_pk = b''
   >>> tx = GEODE.Portal.contract.function.blameOperator(sample_pk).buildTransaction('from': '<myEthereumAddress>')
   >>> tx['nonce'] = GEODE.w3.eth.get_transaction_count('<myEthereumAddress>')
   >>> signed = GEODE.w3.eth.account.sign_transaction(tx, '<YOUR_PRIVATE_KEY>')
   >>> tx_hash = GEODE.w3.eth.sendRawTransaction(signed.rawTransaction)

.. note::

  Geode-Py's property functions are not expensive because they return local variables. 
  These variables are automatically updated every 60 (``REFRESH_RATE``) seconds.


