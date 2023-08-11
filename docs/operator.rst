.. _operators:

Operator
====================

Initilization
--------------------------------------------------

.. py:method:: Geode.Portal.operator(operatorID: int)

Initilize the Operator object of Geode.

.. code-block:: python

    >> geode = Geode(exec_api, cons_key)
    ## You need operator id to create operator object
    >> operatorID = 114..151
    >> myOperator = geode.Portal.operator(operatorID)


Operator Ownership
----------------------------------

.. py:method:: NAME
  ..py:property::


``NAME`` is the name of the operator.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("NAME:",myOperator.NAME)
    NAME: IceBear

.. py:method:: CONTROLLER
  ..py:property::

``CONTROLLER`` ethereum address of the current owner.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("CONTROLLER:",myOperator.NAME)
    CONTROLLER: '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'


.. py:method:: initiated
  ..py:property::


``initiated`` (uint256) is timestamp of initiation time.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("initiated:",myOperator.initiated)
    initiated: 1677379164


.. py:method:: maintainer
  ..py:property::


``maintainer`` (address) is the address of the maintainer.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("maintainer:",myOperator.maintainer)
    maintainer: 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C


Opeartor Fee
-------------

If the operator owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the users momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave operators according to their own interests.


.. WARNING::
    ``fee`` changes takes effect after 3 days.

.. py:method:: fee
  ..py:property::


 Returns ``fee``(uint256) How much of the percentage from maintanence fee will received by the operator. DENOMINATOR: 1e10 (100%).

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("fee:",myOperator.fee)
    fee: 600000000

.. py:method:: priorFee
  ..py:property::

``priorFee`` replaces ``fee`` when ``feeSwitch`` has reached.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("priorFee:", myOperator.priorFee)
    priorFee: 0

.. py:method:: feeSwitch
  ..py:property::

``feeSwitch`` is effective until 3 days.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("feeSwitch:",myOperator.feeSwitch)
    feeSwitch: 0


Operator Periods
--------------------

.. WARNING::
    ``period`` changes takes effect after 3 days.

.. py:method:: periodSwitch
  ..py:property::

``periodSwitch``

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("periodSwitch:",myOperator.periodSwitch)
    periodSwitch: 0

.. py:method:: priorPeriod
  ..py:property::

``priorPeriod``

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("priorPeriod:",myOperator.priorPeriod)
    priorPeriod: 0

.. py:method:: validatorPeriod
  ..py:property::

``validatorPeriod``

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("validatorPeriod:",myOperator.validatorPeriod)
    validatorPeriod: 0

Internal Wallet
-------------------

.. NOTE::
    Every Validator proposal costs 1 Ether, which will be spent from your internal wallet.
    However, ether is returned if the proposal is approved and the validator creation is finalized.

.. py:method:: wallet
  ..py:property::

``wallet`` how much ether (in wei) stored in operators internal wallet.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("wallet:",myOperator.wallet)
    wallet: 0


Prison
-------

To understand why some operators have prisoned read `this link <https://docs.geode.fi/operator-marketplace/regulating-the-marketplace>`_.

.. py:method:: release
  ..py:property::

``release`` is the timestamp of their release time. Governance may release operators if no harm is intended.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("release:",myOperator.release)
    wallet: 0  ## means never prisoned.