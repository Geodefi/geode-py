.. _exceptions:


Exceptions
===============

.. py:exception:: PythonVersionException

    Raises whenPython ``Current version is < 3.7 or > 3.10`` 

.. py:exception:: UnknownChainException

    Raises when ``Provided RPC points to an unknown chainId`` 

.. py:exception:: UnexpectedResponseException

    Raises when ``Https call resulted with an error code (non 2xx)`` 

.. py:exception:: HTTPRequestException

    Raises when ``RESPONSE IS NOT CODE 200`` 

.. py:exception:: MaxAttemptException

    Raises when ``MULTIPLE ATTEMPT MADE BUT CALL FAILED`` 

.. py:exception:: DepositSizeException

    Raises when ``DEPOSIT SIZE IS NOT CORRECT !(1/31) !(1/31)`` 

.. py:exception:: WithdrawalCredentialException

    Raises when ``INCORRECT withdrawal_credentials`` 

.. py:exception:: GenesisForkException

    Raises when ``INCORRECT fork_version`` 

.. py:exception:: NetworkNameException

    Raises when ``INCORRECT network_name`` 

.. py:exception::  DepositDataException

    Raises when ``CAN NOT VERIFY DEPOSIT DATA`` 
