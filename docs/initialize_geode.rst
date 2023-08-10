.. _initilize_geode:


Initilize Geode
====================
# TODO: .env creation

EXECUTION_API
-------------------

.. NOTE:: 
    ``EXECUTION_API`` is your port to connect to ethereum to create the Geode object.
    It is a rpc endpoint as HTTPprovider. 
    If you are running your own node, you can write your own local RPC endpoint, otherwise
    you can reach the node by getting an API key from `Alchemy <https://www.alchemy.com/>`_.

.. code-block:: shell

   $ export EXECUTION_API = "https://eth-goerli.g.alchemy.com/v2/xxxxxxxxxxxxxxxxxxxxxxxxx"


CONSENSUS_KEY
-------------------

.. NOTE:: 
    ``CONSENSUS_KEY`` is required to make beacon chain API requests. 
    You can get it from `beaconcha.in <https://beaconcha.in/pricing>`_ for free.

.. code-block:: shell

   $ export CONSENSUS_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"


.. WARNING:: 
    Please store your ``EXECUTION_API`` and ``CONSENSUS_KEY`` as environmental variable. 
    Do not explicitly use in production code.

Initilize Geode
-------------------

The snippet initializes the Geodefi library by importing the ``Geode`` class from the geode module. It creates an instance of Geode and passes the ``EXECUTION_API`` and ``CONSENSUS_KEY`` values as arguments to the constructor.

.. code-block:: python

    # Get keys from enviroment
    >>> import os
    >>> EXECUTION_API = os.environ['EXECUTION_API']
    >>> CONSENSUS_KEY = os.environ['CONSENSUS_KEY']

    # Initilize Geode
    >>> from geode import Geode
    >>> G = Geode(exec_api = EXECUTION_API, cons_key = CONSENSUS_KEY)

      INFO : Connected to beconcha.in:https://goerli.beaconcha.in/api/v1/

Example: Locally Generating an ID
----------------

You can easily get id of the specific role by typing name of it.
First, it imports the generateId function from the geode.utils module and the ``ID_TYPE`` enumeration from the geode.globals module.

.. code-block:: python

    >>> from geode.utils import generateId
    >>> from geode.globals import ID_TYPE

    # Get ID of a pool that named "Ice Bear's Pool"
    # Pools id is 5 by default, so ID_TYPE.POOL => 5
    >>> generateId("Ice Bear's Pool", ID_TYPE.POOL)
      50016835115526216130031110555486827201953559012021267556883950029143900999178

    # Generate Operator ID
    >>> generateId("IceBear", ID_TYPE.OPERATOR)
      114391297015478800753082638170652680401082080549997516459063441314156612391510


    >>> pid = 50016835115526216130031110555486827201953559012021267556883950029143900999178
    >>> oid = 114391297015478800753082638170652680401082080549997516459063441314156612391510
    

Create Objects
-----------------

This code snippet showcases the usage of the Geodefi library. 
It initializes the ``Beacon`` and ``Portal`` objects, representing key components of Geodefi. 
Additionally, it creates a gETH object that represents the ``gETH`` token. The snippet also demonstrates how to retrieve information about a pool using the pool() function, identified by pid, and how to retrieve information about an operator using the operator() function, identified by oid.

.. code-block:: python

    >>> Beacon = G.Beacon

    >>> Portal = G.Portal
      INFO : Portal:goerli head is on 'v1'

    >>> gETH = G.Token
      INFO : Token:gETH
    
    >>> myPool = G.Portal.pool(pid)
      INFO : ID TYPE:POOL:50016835115526216130031110555486827201953559012021267556883950029143900999178
    
    >>> myOperator = G.Portal.operator(oid)
      INFO : ID TYPE:OPERATOR:114391297015478800753082638170652680401082080549997516459063441314156612391510
