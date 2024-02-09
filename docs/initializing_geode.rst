.. _initializing_geode:


Initializing Geode
====================

ENVIROMENTAL VARIABLES
*************************

 A ``env`` file is a configuration file to store sensitive environment variables, separated from the codebase. 

.. code-block:: shell

  EXECUTION_API = "https://xxxxxxxx.ethereum-holesky.quiknode.pro/xxxxxxxx"
  CONSENSUS_API = "https://holesky.beaconstate.ethstaker.cc" # prefferably use your local (exposed) node
  PRIVATE_KEY = "586acb3c6bac489308c0938f762da702573a714dfdf3a729dcb40758b4c363ae" # optional


PRIVATE_KEY
-------------------

.. WARNING:: 
  Be mindful of version control systems and sharing mechanisms to prevent accidental exposure of ``PRIVATE_KEY``. 
  It is crucial to avoid using generic or predictable names, such as ``PRIVATE_KEY`` for your private keys within your codebase or configuration files.
  Doing so could potentially make it easier for malicious actors to identify and exploit these keys if they gain access to your source code. 
  Instead, use unique and descriptive names for your private keys, and consider storing them securely in environment variables.

.. NOTE::
  If the ``PRIVATE_KEY`` was not set, it is still possible to use all view functions in Geode contracts. Please consider your application carefully before the creating .env.
    

EXECUTION_API
-------------------

.. NOTE:: 
    ``EXECUTION_API`` is your port to connect to ethereum to create the Geode object.
    It is a rpc endpoint as HTTPprovider. 
    If you are running your own node, you can write your own local RPC endpoint, otherwise
    you can reach the node by getting an API key from `Alchemy <https://www.alchemy.com/>`_.

.. code-block:: shell

   $ export EXECUTION_API = "https://xxxxxxxx.ethereum-holesky.quiknode.pro/xxxxxxxx"

CONSENSUS_API
-------------------

.. NOTE:: 
    ``CONSENSUS_API`` is required to make beacon chain API requests.

.. code-block:: shell

   $ export CONSENSUS_API = "https://holesky.beaconstate.ethstaker.cc"


.. WARNING:: 
    Please store your ``EXECUTION_API`` and ``CONSENSUS_API`` as environmental variable. 
    Do not explicitly use in production code.

Initilizing Geode Object
*************************

The snippet initializes the Geodefi library by importing the ``Geode`` class from the geode module. It creates an object of Geode and passes the ``EXECUTION_API`` and ``CONSENSUS_API`` values as arguments to the constructor.

.. code-block:: python

    # Get keys from enviroment
    >>> import os
    >>> EXECUTION_API = os.environ['EXECUTION_API']
    >>> CONSENSUS_API = os.environ['CONSENSUS_API']

    # Initilize Geode
    >>> from geode import Geode
    >>> G = Geode(exec_api = EXECUTION_API, cons_api = CONSENSUS_API)

      INFO : Connected to beconcha.in: https://holesky.beaconstate.ethstaker.cc


Configuration for Geode Object
********************************

Configure parameters such as ``MAX_ATTEMPT``, ``ATTEMPT_RATE``, and ``REFRESH_RATE`` to fine-tune performance for your specific use case.

.. code-block:: python

    >>> import logging

    ## You can config the logging to get detailed outputs
    >>> logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(message)s')

    >>> G.MAX_ATTEMPT = 10 # request will fail after 10 calls.
    >>> G.ATTEMPT_RATE = 0.1  # interval between calls (in seconds)
    >>> G.REFRESH_RATE = 60  # cached data will be refreshed after 60 seconds


Understanding Geodefi Classes
******************************

This code snippet showcases the usage of the Geodefi library. 
It initializes the ``Beacon`` and ``Portal`` objects, representing key components of Geodefi. 
Additionally, it creates a ``gETH`` token object that represents the gETH token on ethereum. The snippet also demonstrates how to retrieve information about a pool using the pool() function, identified by pid, and how to retrieve information about an operator using the operator() function, identified by oid.


.. py:class:: geode.Geode(exec_key, cons_api)

Each ``Geode`` instance has following sub-classes

.. py:class:: geode.Geode.Portal()
  
  To manage all Portal contract functionalities.

.. py:class:: geode.Geode.Token.()

  To manage all chain agnostic token functionalities.

.. py:class:: geode.Geode.Beacon()

  To manage all beacon chain api requests.

.. py:class:: geode.Portal.Pool()

  To manage all Pool functionalities.

.. py:class:: geode.Portal.Operator()

  To manage all Operator functionalities.


.. code-block:: python

    >>> Beacon = G.Beacon

    >>> Portal = G.Portal
      INFO : Portal:holesky head is on 'v1'

    >>> gETH = G.Token
      INFO : Token:gETH
    
    >>> myPool = G.Portal.pool(pid)
      INFO : ID TYPE:POOL:50016835115526216130031110555486827201953559012021267556883950029143900999178
    
    >>> myOperator = G.Portal.operator(oid)
      INFO : ID TYPE:OPERATOR:114391297015478800753082638170652680401082080549997516459063441314156612391510
