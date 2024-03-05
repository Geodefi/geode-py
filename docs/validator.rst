.. _validator:

Validator
=========

.. py:module:: Validator
.. py:currentmodule:: Validator

.. contents:: :local:

Create a Validator Instace
--------------------------

-------------------------------
From a Pool Instance with Index
-------------------------------

.. py:method:: Portal.pool.validators(index: uint256)

  Returns a ``Validator`` object of the pool by the given index.

  .. code-block:: python

    # Check Pools page to create myPool object.
    validator = myPool.validators(index=1)

-----------------------------------
Get Validator Details with a Pubkey
-----------------------------------

.. py:method:: Portal.pool.getValidator(pubkey: hex-str)

  Returns the ``Validator`` object for the given pubkey.

  .. code-block:: python

    pubkey = "0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d"
    myVal = Portal.functions.getValidator(pubkey)

----

Validator Data from Beacon Chain
--------------------------------

.. WARNING::
  Once the validator is proposed, configuration parameters on the portal can't be mutated.

.. py:property:: status

  Returns the ``status`` string like 'active' or 'active_ongoing' etc. This data is obtained from beacon chain.

  .. code-block:: python

    myVal.status
    # active_offline

.. py:property:: beacon_index

  Returns the ``index`` integer value, which is obtained from beacon chain.

  .. code-block:: python

    myVal.beacon_index
    # 441075

.. py:property:: withdrawal_credentials

  Returns the ``withdrawal_credentials`` as bytes32 value of the validator. For a validator created through Geodefi this should point to the Pool's withdrawal contract.
    
  .. code-block:: python

    myVal.withdrawal_credentials
    # '0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e'

.. py:property:: balance

  Returns the ``balance`` integer of the epoch which validator will be exited.

  .. code-block:: python

    myVal.balance
    # 31896486280

.. py:property:: effective_balance

  Returns the ``effectivebalance`` integer of the epoch which validator will be exited.
 
  .. code-block:: python

    myVal.effectivebalance
    # 32000000000

.. py:property:: slashed

  Returns the ``slashed`` bool value. 

  .. code-block:: python

    myVal.slashed
    # False

.. py:property:: activation_eligibility_epoch

  Returns the ``activation_eligibility_epoch`` integer value. 

  .. code-block:: python

    myVal.activation_eligibility_epoch
    # 35720

.. py:property:: exit_epoch

  Returns the ``exit_epoch`` integer value. 

  .. code-block:: python

    myVal.exit_epoch
    # 35720

.. py:property:: withdrawable_epoch

  Returns the ``withdrawable_epoch`` integer value. 

  .. code-block:: python

    myVal.withdrawable_epoch
    # 35720

----

Validator Data from Portal
--------------------------

.. py:property:: portal_index

  Returns the ``portal_index`` integer value. This index used increases linearly as more validators are created through Geodefi.

  .. code-block:: python

    myVal.portal_index
    # 1

.. py:property:: state

  Returns the ``state`` enumarate like ``VALIDATOR_STATE.ACTIVE``

  .. code-block:: python

    # get a state of validator
    myVal.state
    # VALIDATOR_STATE.ACTIVE

* ``VALIDATOR_STATE`` enums

  .. code-block:: python

          NONE = 0
          # invalid

          PROPOSED = 1
          # validator is proposed, 1 ETH is sent from Operator to Deposit Contract.

          ACTIVE = 2
          # proposal was approved, operator used pooled funds, 1 ETH is released back to Operator.
          
          EXIT_REQUESTED = 3
          # validator is called to be exited.

          EXITED = 4
          # validator is fully exited.

          ALIENATED = 69
          # proposal was malicious(alien). Maybe faulty signatures or probably frontrunning (https://bit.ly/3Tkc6UC)

.. py:property:: createdAt

  Returns ``createdAt`` (uint256) At what timestamp validator has created.

  .. code-block:: python

    myVal.createdAt
    # 1695632168

.. py:property:: period

  Returns ``period`` (uint256) 

  .. code-block:: python

    myVal.period
    # 500000000

.. py:property:: poolId

  Returns the ``poolID`` large integer value.

  .. code-block:: python

    myVal.poolID
    # 50016835115526216130031110555486827201953559012021267556883950029143900999178

.. py:property:: opeartorId

  Returns the ``opeartorId`` large integer value.

  .. code-block:: python

    myVal.opeartorId
    # 114391297015478800753082638170652680401082080549997516459063441314156612391510


.. py:property:: poolFee

  Returns ``poolFee`` (uint256) How much of the percentage from maintanence fee will received by the pool owner. DENOMINATOR: 1e10 (100%).

  .. code-block:: python

    myVal.poolFee
    # 500000000

.. py:property:: operatorFee

  Returns ``operatorFee`` (uint256) How much of the percentage from maintanence fee will received by the operator. DENOMINATOR: 1e10 (100%).

  .. code-block:: python

    myVal.operatorFee
    # 500000000

.. py:property:: infrastructureFee

  Returns ``infrastructureFee`` (uint256) How much of the percentage from the validator yield that will received by the Governance. Note that PERCENTAGE_DENOMINATOR = 1e10 (100%).

  .. code-block:: python

    myVal.infrastructureFee
    # 500000000

.. py:property:: signature31

  Returns the ``signature31`` bytes32 to ensures 2-step validator creation.

  .. code-block:: python

    # as bytes
    myVal.signature31
    # b'\x94\xc0\x18~I\x0e\xc3\x96r&\xd3\xc3\xce\xbc\xf0\xb0t\xbf\xa0Iq\xe5+\x95t\x8e\x91\x93?\x93\xfc?\x93g}\x94tM\xf5 \x89|\x99\xd3sn\xd1\xdb\x08\xa8!i\x813\xc2b\xb3SdB\x95Y\xa1\xb0z\xc4\x85`\xd2z.g\x88Dq\xf8R/g\xae\nB\xfa\xaa\xee!~\x9c@\xe0\\\xd91(\xad\xdb'

    # as Hexstring
    myVal.signature31.hex()
    # '94c0187e490ec3967226d3c3cebcf0b074bfa04971e52b95748e91933f93fc3f93677d94744df520897c99d3736ed1db08a821698133c262b35364429559a1b07ac48560d27a2e67884471f8522f67ae0a42faaaee217e9c40e05cd93128addb'