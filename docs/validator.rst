.. _validators:

Beacon 
==============

.. py:class:: geode.Beacon()

.. NOTE::

    This class has some of the api endpoints for https://beaconcha.in/ implemented. Not all, just the ones we think is currently needed. But we are planning to implement all of them in the next release.
    Visit https://goerli.beaconcha.in/api/v1/docs/index.html#/ for all.


Initilization
-----------------

.. code-block:: python

    >>> Beacon = geode.Beacon

API Requests
----------------------------

.. py:method:: Beacon.get_validator_eth1(eth1: address)

Get all validators that belong to an eth1 address.

.. code-block:: python

    >>> Beacon.get_validator_eth1(eth1)
        {
        "data": [
            {
            "public_key": "string",
            "valid_signature": true,
            "validator_index": 0
            }
        ],
        "status": "string"
        }

.. py:method:: Beacon.get_validator_withdrawalCredentials(eth1: address)

Get all validator indexes and pubkeys of withdrawal credentials or eth1 address.

.. code-block:: python

    >>> Beacon.get_validator_withdrawalCredentials(eth1)
        {
        "data": [
            {
            "publickey": "string",
            "validatorindex": 0
            }
        ],
        "status": "string"
        }


.. py:method:: Beacon.get_validator(pubkey: hexstr)

Get up to 100 validator

.. code-block:: python

    >>> Beacon.get_validator(pubkey)
        { 
        "data": [
            {
            "activation_eligibility_epoch": 0,
            "activation_epoch": 0,
            "balance": 0,
            "effective_balance": 0,
            "exit_epoch": 0,
            "last_attestation_slot": 0,
            "name": "string",
            "pubkey": "string",
            "slashed": true,
            "status": "string",
            "validator_index": 0,
            "withdrawable_epoch": 0,
            "withdrawal_credentials": "string"
            }
        ],
        "status": "string"
        }

.. py:method:: Beacon.get_validator_balancehistory(pubkey: hexstr)

Get balance history up to 100 validator

.. code-block:: python

    >>> Beacon.get_validator_balancehistory(pubkey)
       {
        "data": [
            {
            "balance": 0,
            "effectivebalance": 0,
            "epoch": 0,
            "validatorindex": 0,
            "week": 0,
            "week_end": "string",
            "week_start": "string"
            }
        ],
        "status": "string"
        }

.. py:method:: Beacon.get_validator_deposits(pubkey: hexstr)

Get all eth1 deposits for up to 100 validators.

.. code-block:: python

    >>> Beacon.get_validator_deposits(pubkey)
       {
        "data": [
            {
            "amount": 0,
            "block_number": 0,
            "block_ts": 0,
            "from_address": "string",
            "merkletree_index": "string",
            "publickey": "string",
            "removed": true,
            "signature": "string",
            "tx_hash": "string",
            "tx_index": 0,
            "tx_input": "string",
            "valid_signature": true,
            "withdrawal_credentials": "string"
            }
        ],
        "status": "string"
        }

.. py:method:: Beacon.get_validator_withdrawals(pubkey: hexstr)

Get the withdrawal history up to 100 validators.

.. code-block:: python

    >>> Beacon.get_validator_withdrawals(pubkey)
       {
        "data": [
            {
            "address": "string",
            "amount": 0,
            "blockroot": "string",
            "epoch": 0,
            "slot": 0,
            "validatorindex": 0,
            "withdrawalindex": 0
            }
        ],
        "status": "string"
        }

.. py:method:: Beacon.get_eth1deposit(tx: hexstr)

Get an eth1 deposit by its eth1 transaction hash.

.. code-block:: python

    >>> Beacon.get_eth1deposit(pubkey)
       {
        "data": "string",
        "status": "string"
        }


.. py:method:: Beacon.get_validators_queue()

Get current validator queue.

.. code-block:: python

    >>> Beacon.get_validators_queue()
       {
        "data": "string",
        "status": "string"
        },
        {
        "data": {
            "beaconchain_entering": 0,
            "beaconchain_exiting": 0,
            "validators_count": 0
        },
        "status": "string"
        }

Validator 
==============

Initilization
----------------------------

.. py:class:: Portal.pool.validators(index: uint256)

    Returns the ``Validator`` object of the pool by the given index.

.. code-block:: python

    # Check Pools page to create myPool object.
    # get a Portal address
    >>> myVal = myPool.validators(0)

* Alternatively, read validator details directly from Portal with a pubkey.

.. py:method:: Portal.pool.getValidator(pubkey: hex-str)

    Returns the ``Validator`` object of the pool by the given index.

.. code-block:: python

    # Check Pools page to create myPool object.
    # get a Portal address
    >>> pubkey = "0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d"
    >>> myVal = Portal.functions.getValidator(pubkey)


Validator Data from Beacon
----------------------------

.. WARNING::
    Once the validator is proposed, it is logged and its parameters do not change again.


.. py:method:: PORTAL.pool.validators(index: uint256).status

    Returns the ``status`` string like 'active' or 'active_ongoing' etc. This data is obtained from beacon chain.

.. code-block:: python

    # get a state of validator
    >>> myVal.status
    active_offline


.. py:method:: PORTAL.pool.validators(index: uint256).validatorindex

    Returns the ``index`` integer value. This index has obtained from beacon chain.

.. code-block:: python

    >>> myVal.validatorindex
    441075


.. py:method:: PORTAL.pool.validators(index: uint256).withdrawalCredentials

    Returns the ``withdrawalCredentials`` bytes32 value of withdrawal credentials.
    
.. code-block:: python

    >>> myVal.withdrawalCredentials
    '0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e'


.. py:method:: PORTAL.pool.validators(index: uint256).balance

    Returns the ``balance`` integer of the epoch which validator will be exited.
.. code-block:: python

    >>> myVal.balance
    31896486280


.. py:method:: PORTAL.pool.validators(index: uint256).effectivebalance

    Returns the ``effectivebalance`` integer of the epoch which validator will be exited.
.. code-block:: python

    >>> myVal.effectivebalance
    32000000000

.. py:method:: PORTAL.pool.validators(index: uint256).totalWithdrawals

    Returns the ``totalWithdrawals`` integer of the epoch which validator will be exited.
.. code-block:: python

    >>> myVal.totalWithdrawals
    36846076


.. py:method:: PORTAL.pool.validators(index: uint256).slashed

    Returns the ``slashed`` bool value. 

.. code-block:: python

    >>> myVal.slashed
    False


Validator Data from Portal
----------------------------

.. py:method:: PORTAL.pool.validators(index: uint256).state

    Returns the ``state`` enumarate like ``VALIDATOR_STATE.ACTIVE``

.. code-block:: python

    # get a state of validator
    >>> myVal.state
    VALIDATOR_STATE.ACTIVE

* ``VALIDATOR_STATE`` enums

.. code-block:: python

        # invalid
        NONE = 0
        # validator is proposed, 1 ETH is sent from Operator to Deposit Contract.
        PROPOSED = 1
        # proposal was approved, operator used pooled funds, 1 ETH is released back to Operator.
        ACTIVE = 2
        # validator is called to be exited.
        EXIT_REQUESTED = 3
        # validator is fully exited.
        EXITED = 4
        # proposal was malicious(alien). Maybe faulty signatures or probably frontrunning (https://bit.ly/3Tkc6UC)
        ALIENATED = 69


.. py:method:: PORTAL.pool.validators(index: uint256).index

    Returns the ``index`` integer value. This index used inside Geode Contracts.

.. code-block:: python

    >>> myVal.index
    1


.. py:method:: PORTAL.pool.validators(index: uint256).poolId

    Returns the ``poolID`` large integer value.

.. code-block:: python

    >>> myVal.poolID
    50016835115526216130031110555486827201953559012021267556883950029143900999178


.. py:method:: PORTAL.pool.validators(index: uint256).opeartorId

    Returns the ``opeartorId`` large integer value.

.. code-block:: python

    >>> myVal.opeartorId
    114391297015478800753082638170652680401082080549997516459063441314156612391510


.. py:method:: PORTAL.pool.validators(index: uint256).poolFee

    Returns ``poolFee`` (uint256) How much of the percentage from maintanence fee will received by the pool owner. DENOMINATOR: 1e10 (100%).

.. code-block:: python

    >>> myVal.poolFee
    500000000

.. py:method:: PORTAL.pool.validators(index: uint256).operatorFee

    Returns ``operatorFee`` (uint256) How much of the percentage from maintanence fee will received by the operator. DENOMINATOR: 1e10 (100%).

.. code-block:: python

    >>> myVal.operatorFee
    500000000

.. py:method:: PORTAL.pool.validators(index: uint256).governanceFee

    Returns ``governanceFee`` (uint256) How much of the percentage from maintanence fee will received by the Governance. DENOMINATOR: 1e10 (100%).

.. code-block:: python

    >>> myVal.governanceFee
    500000000

.. py:method:: PORTAL.pool.validators(index: uint256).createdAt

    Returns ``createdAt`` (uint256) At what timestamp validator has created.

.. code-block:: python

    >>> myVal.createdAt
    1695632168

.. py:method:: PORTAL.pool.validators(index: uint256).period

    Returns ``period`` (uint256) 

.. code-block:: python

    >>> myVal.period
    500000000


.. py:method:: PORTAL.pool.validators(index: uint256).signature31

    Returns the ``signature31`` bytes32 to ensures 2-step validator creation.
.. code-block:: python

    # Bytes32
    >>> myVal.signature31
    b'\x94\xc0\x18~I\x0e\xc3\x96r&\xd3\xc3\xce\xbc\xf0\xb0t\xbf\xa0Iq\xe5+\x95t\x8e\x91\x93?\x93\xfc?\x93g}\x94tM\xf5 \x89|\x99\xd3sn\xd1\xdb\x08\xa8!i\x813\xc2b\xb3SdB\x95Y\xa1\xb0z\xc4\x85`\xd2z.g\x88Dq\xf8R/g\xae\nB\xfa\xaa\xee!~\x9c@\xe0\\\xd91(\xad\xdb'

    # Hexstring
    >>> myVal.signature31.hex()
    '94c0187e490ec3967226d3c3cebcf0b074bfa04971e52b95748e91933f93fc3f93677d94744df520897c99d3736ed1db08a821698133c262b35364429559a1b07ac48560d27a2e67884471f8522f67ae0a42faaaee217e9c40e05cd93128addb'



    
