.. _configuration:

Configuration
=============

``.env`` file should be utilized to store sensitive information such as your wallet private key or api keys. 

.. code-block:: shell

  EXECUTION_API = "https://rpc.ankr.com/eth_holesky/<<your_key>>" # prefferably use your local execution client
  CONSENSUS_API = "https://rpc.ankr.com/premium-http/eth_holesky_beacon/<<your_key>>" # prefferably use your local (exposed) beacon client
  PRIVATE_KEY = "37f3c21916a128c092fbb204246ae7a9498fdf81d41e76ddc8e3d6e0004af6af" # optional

----

EXECUTION_API
-------------

``EXECUTION_API`` should be an RPC endpoint (https or wss) that will be used with `web3.HTTPprovider` or `web3.WebsocketProvider`.
If you are running your own node, you can provide your local (exposed) RPC endpoint.
Otherwise you can utilize a remote node by getting an API key from third party service providers such as:

- `Ankr <https://www.ankr.com/remote-procedure-call/>`_ (recommended: supports beaconchain queries)

- `Alchemy <https://www.alchemy.com/>`_

- `Infura <https://www.infura.io/>`_

----

CONSENSUS_API
-------------

**geodefi** is not dependant on ``CONSENSUS_API``, meaning some functionalities will persist without it. 
**However,** ``CONSENSUS_API`` **is required to make beacon chain API requests.**

----

PRIVATE_KEY
-----------
**geodefi** is not going to manage your private key as default. However, you can optionally provide it if you want/need to send some transactions. 

.. WARNING:: 
  Be mindful of version control systems and sharing mechanisms to prevent accidental exposure of ``PRIVATE_KEY``. 
  It is crucial to avoid using generic or predictable names, such as ``PRIVATE_KEY`` for your private keys within your codebase or configuration files.
  Doing so could potentially make it easier for malicious actors to identify and exploit these keys if they gain access to your source code. 
  Instead, use unique and descriptive names for your private keys, and consider storing them securely in environment variables.


| Successfully configured.
| **Next step: start coding by initializing the geodefi package.**