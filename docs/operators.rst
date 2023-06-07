.. _operators:

Operators
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


General Information of Operator
----------------------------------

NAME
******************

``NAME`` is the name of the operator that given from creator of the pool.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("NAME:",myOperator.NAME)
    NAME: IceBear


CONTROLLER
----------------

``CONTROLLER`` ethereum address of the controller of the operator


.. code-block:: python


    >> myOperator = geode.Portal.operator(operatorID)
    >> print("CONTROLLER:",myOperator.NAME)
    CONTROLLER: '0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C'

initiated
--------------------------------------------------

``initiated`` (uint256) is timestamp of initiation time.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("initiated:",myOperator.initiated)
    initiated: 1677379164

maintainer
--------------------------------------------------

``maintainer`` (address) is the address of the maintainer.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("maintainer:",myOperator.maintainer)
    maintainer: 0x2C95BC18Fd9382a07776D416EeF6c2FEb3AD2A8C


Fee
**********************************************

If the operator owner or maintainer wants to update its ``fee``, the operations continue from the value named ``priorFee`` for a certain period of time after the fee changes so that it does not manipulate the users momentarily. This period is 3 days and must be kept in the variable named ``feeSwitch``. At the end of the ``feeSwitch`` period, the updated ``fee`` comes into play, so users have the freedom to leave operators according to their own interests.


fee
--------------------------------------------------

``fee``(uint256) How much commission the operator will take? DENOMINATOR: 1e9

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("fee:",myOperator.fee)
    fee: 500000000

priorFee
--------------------------------------------------

``priorFee`` replaces ``fee`` in ``feeSwitch`` period.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("priorFee:", myOperator.priorFee)
    priorFee: 0


feeSwitch
--------------------------------------------------

``feeSwitch`` is the block period, corresponds to 3 days.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("feeSwitch:",myOperator.feeSwitch)
    feeSwitch: 0


Validators
********************************

totalActiveValidators
--------------------------------------------------

``totalActiveValidators`` (uint256) how many validator is currently operating.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("totalActiveValidators:",myOperator.totalActiveValidators)
    
    totalActiveValidators: 1


totalProposedValidators
--------------------------------------------------

``totalProposedValidators`` (uint256) how many validator has been proposed.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("totalProposedValidators:",myOperator.validatorsLen)
    
    totalProposedValidators: 0


validatorPeriod
--------------------------------------------------

``validatorPeriod`` (uint256) how many validator has been proposed.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("validatorsLen:",myOperator.validatorsLen)
    
    validatorsLen: 1

totalProposedValidators
--------------------------------------------------

``totalProposedValidators`` (uint256) how many validator has been proposed.

.. code-block:: python

    >> myOperator = geode.Portal.operator(operatorID)
    >> print("validatorsLen:",myOperator.validatorsLen)
    
    validatorsLen: 1