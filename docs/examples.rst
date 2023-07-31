.. _examples:


Examples
===============

How to get all operators
How to get all validators
How to get all planets
How to propose operator
How to alienate a validator

How to get all pubkeys
***********************

.. code-block:: python

    >> myPool = geode.Portal.pool(poolID)
    >> number_of_validators = myPool.validatorsLen
    >> for validator in range(number_of_validators)
    
    fee: 500000000