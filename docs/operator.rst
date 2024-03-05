.. _operator:

Operator
========

.. py:module:: Operator
.. py:currentmodule:: Operator

.. contents:: :local:

Create an Operator Instace
--------------------------

.. py:method:: Geode.Portal.operator(operatorID: int)

Initilize the Operator object with an existing operator id:

  .. code-block:: python

    # You need operator id to create operator object
    operatorID = 500191....78
    myOperator = geode.Portal.operator(operatorID)


Operator Ownership
------------------

.. py:property:::: NAME

  ``NAME`` is the name of the operator.

  .. code-block:: python

    myOperator.NAME
    # Ice Bear's Operator

.. py:property:: CONTROLLER

  ``CONTROLLER`` ethereum address of the controller of the Operator

  .. code-block:: python

    myOperator.CONTROLLER
    # 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C

.. py:property:: initiated

  ``initiated`` (uint256) is timestamp of initiation time.

  .. code-block:: python

    myOperator.initiated
    # 1677379164 
    # (unix seconds)

.. py:property:: maintainer

  ``maintainer`` (address) is the address of the maintainer, set by the owner. Handles day to day operations like creation of validators.

  .. code-block:: python

    myOperator.maintainer
    # 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C

Operator Fee
----------------------

If the operator owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the users momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave operators according to their own interests.

.. WARNING::
  ``period`` changes takes effect after 3 days.

.. py:property:: fee

  Returns ``fee`` (uint256) How much of the percentage from validator yield will received by the operator CONTROLLER. DENOMINATOR: 1e10 (100%).

  .. code-block:: python

    myOperator.fee
    # 500000000
    # PERCENTAGE_DENOMINATOR = 100%

  .. NOTE::
      If the Operator owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the pool momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave the pool according to their own interests.

.. py:property:: priorFee

  ``priorFee`` replaces ``fee`` when ``feeSwitch`` is reached.

  .. code-block:: python

    myOperator.priorFee    
    # 400000000
    # PERCENTAGE_DENOMINATOR = 100%

.. py:property:: feeSwitch

  ``feeSwitch`` is set to 3 days after the function call, meaning there will be 3 days delay on every time fee is changed.

  .. code-block:: python

    myOperator.feeSwitch
    # 1709191201
    # (unix seconds)

Validator Period
--------------------

An Operator's ``validatorPeriod`` can be chosen between ``90 - 720 days`` , and should be defined in seconds.

.. WARNING::
  | When a Operator's period is changed, it takes 3 days for new period to take effect. 
  | Within this 3 day time span, the period can not be changed again.
  | However, you can stop proposing new validators before your cool-down period ends.

.. py:property:: validatorPeriod

  .. code-block:: python

    myOperator.validatorPeriod
    # 157680000 / 2 years in seconds

.. py:property:: priorPeriod

  .. code-block:: python

    myOperator.priorPeriod
    # 7776000 / 90 days

.. py:property:: periodSwitch

  ``periodSwitch`` defines the latest unix timestamp when the ``validatorPeriod`` will be effective instead of ``priorPeriod`` 

  .. code-block:: python

    myOperator.periodSwitch
    # 1709537189

Internal Wallet
---------------

.. NOTE::
    Every Validator proposal requires 1 Ether, which will be spent from your internal wallet.
    However, this amount is returned if the proposal is approved and the validator creation is finalized.

.. py:property:: wallet

  | Every ID has its own internal wallet within Portal. 
  | It accrues fees, makes things safer and easier for Node Operators when creating validators etc. 
  | ``wallet`` (uint256) amount (in ``wei``) in the internal wallet of the Operator.
  
  .. code-block:: python

    myOperator.wallet
    # wallet: 10000000000000
    # (as wei) (1e18 = 1 ether)

  .. note:: 
    | ``CONTROLLER`` of an ID can increase the internal wallet by depositing ether with ``portal.functions.increaseWalletBalance(id)``.
    | Also, can decrease by reclaiming the ether that is accrued with ``portal.functions.decreaseWalletBalance(id)``.

Prison
-------

To understand why some operators have prisoned read `this link <https://docs.geode.fi/operator-marketplace/regulating-the-marketplace>`_.

.. py:property:: release

  ``release`` is the timestamp of their release time. Governance may release operators if no harm is intended.

  .. code-block:: python

    myOperator.release
    # 0 # never prisoned

More 
----

Next step: Learn how to create validators through geodefi: :ref:`creating_validators`
