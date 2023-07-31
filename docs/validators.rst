.. _validators:

Validator 
==============


.. py:method:: PORTAL.pool.validators(index: uint256)

    Returns the ``Validator`` object of the pool by the given index.

.. code-block:: python

    # Check Pools page to create myPool object.
    # get a Portal address
    >>> myVal = myPool.validators(0)

Id
------------

.. py:method:: PORTAL.pool.validators(index: uint256).state

    Returns the ``state`` enumarate like ``VALIDATOR_STATE.ACTIVE``

.. code-block:: python

    # get a state of validator
    >>> myVal.state
    VALIDATOR_STATE.ACTIVE

.. py:method:: PORTAL.pool.validators(index: uint256).status

    Returns the ``status`` string like 'active' or 'active_ongoing' etc. This data is obtained from beacon chain.

.. code-block:: python

    # get a state of validator
    >>> myVal.status
    active_offline

.. py:method:: PORTAL.pool.validators(index: uint256).index

    Returns the ``index`` integer value. This index used inside Geode Contracts.

.. code-block:: python

    >>> myVal.index
    1

.. py:method:: PORTAL.pool.validators(index: uint256).validatorindex

    Returns the ``index`` integer value. This index has obtained from beacon chain.

.. code-block:: python

    >>> myVal.validatorindex
    441075

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


.. py:method:: PORTAL.pool.validators(index: uint256).slashed

    Returns the ``slashed`` bool value. 

.. code-block:: python

    >>> myVal.slashed
    False





Fee Related
------------

.. py:method:: PORTAL.pool.validators(index: uint256).poolFee

    Returns the ``poolFee`` integer value to show how much commission will pool takes from this validator's profit. DENOMINATOR:1e9

.. code-block:: python

    >>> myVal.poolFee
    500000000

.. py:method:: PORTAL.pool.validators(index: uint256).operatorFee

    Returns the ``operatorFee`` integer value to show how much commission will operator takes from this validator's profit. DENOMINATOR:1e9

.. code-block:: python

    >>> myVal.operatorFee
    500000000

.. py:method:: PORTAL.pool.validators(index: uint256).earlyExitFee

    Returns the ``earlyExitFee`` integer value to show what percentage will be penailtized in case of early exit.

.. code-block:: python

    >>> myVal.earlyExitFee
    0


Timestamps
------------

.. py:method:: PORTAL.pool.validators(index: uint256).createdAt

    Returns the ``createdAt`` timestamp value to indicate creation time of validator.

.. code-block:: python

    >>> myVal.createdAt
    1677383052

.. py:method:: PORTAL.pool.validators(index: uint256).expectedExit

    Returns the ``expectedExit`` timestamp value to indicate time the validator plans to exit.

.. code-block:: python

    >>> myVal.expectedExit
    1692935052

Signature 31
--------------

.. py:method:: PORTAL.pool.validators(index: uint256).signature31

    Returns the ``signature31`` bytes32 to prevent any harms to system by telescope.
.. code-block:: python

    # Bytes32
    >>> myVal.signature31
    b'\x94\xc0\x18~I\x0e\xc3\x96r&\xd3\xc3\xce\xbc\xf0\xb0t\xbf\xa0Iq\xe5+\x95t\x8e\x91\x93?\x93\xfc?\x93g}\x94tM\xf5 \x89|\x99\xd3sn\xd1\xdb\x08\xa8!i\x813\xc2b\xb3SdB\x95Y\xa1\xb0z\xc4\x85`\xd2z.g\x88Dq\xf8R/g\xae\nB\xfa\xaa\xee!~\x9c@\xe0\\\xd91(\xad\xdb'

    # Hexstring
    >>> myVal.signature31.hex()
    '94c0187e490ec3967226d3c3cebcf0b074bfa04971e52b95748e91933f93fc3f93677d94744df520897c99d3736ed1db08a821698133c262b35364429559a1b07ac48560d27a2e67884471f8522f67ae0a42faaaee217e9c40e05cd93128addb'

Epochs
------------

.. py:method:: PORTAL.pool.validators(index: uint256).activationEligibilityEpoch

    Returns the ``activationEligibilityEpoch`` integer value of activation epoch when the validator is eligible to stake.

.. code-block:: python

    >>> myVal.activationEligibilityEpoch
    158695


.. py:method:: PORTAL.pool.validators(index: uint256).activationEpoch

    Returns the ``activationEpoch`` integer value of epoch that which validator is activated.
    
.. code-block:: python

    >>> myVal.activationEpoch
    159010

.. py:method:: PORTAL.pool.validators(index: uint256).exitepoch

    Returns the ``exitepoch`` integer of the epoch which validator will be exited.
.. code-block:: python

    >>> myVal.exitepoch
    258042

.. py:method:: PORTAL.pool.validators(index: uint256).withdrawableepoch

    Returns the ``withdrawableepoch`` integer of the epoch which validator could withdraw the deposited ether.
.. code-block:: python

    >>> myVal.withdrawableepoch
    9223372036854775807


Balances
------------

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


Withdrawals
-------------------

.. py:method:: PORTAL.pool.validators(index: uint256).withdrawalcredentials

    Returns the ``withdrawalcredentials`` bytes32 value of withdrawal credentials.
    
.. code-block:: python

    >>> myVal.withdrawalcredentials
    '0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e'

.. py:method:: PORTAL.pool.validators(index: uint256).total_withdrawals

    Returns the ``total_withdrawals`` integer of the epoch which validator will be exited.
.. code-block:: python

    >>> myVal.total_withdrawals
    36846076

    
