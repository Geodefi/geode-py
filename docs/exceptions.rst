.. _exceptions:


Exceptions
===============

.. py:method::   class PythonVersionException(Exception)

    Raises when the Python ``VERSION < 3.7`` 

.. py:method::   class UnknownChainException(Exception)

    Raises when ``GIVEN NETWORK IS NOT DEFINED`` 

.. py:method::   class UnexpectedResponseException(Exception)

    Raises when ``CAN NOT HANDLE RESPONSE`` 

.. py:method::   class BadRequestException(Exception)

    Raises when ``RESPONSE IS NOT CODE 200`` 

.. py:method::   class MaxAttemptException(Exception)

    Raises when ``MULTIPLE ATTEMPT MADE BUT CALL FAILED`` 

.. py:method::   class DepositSizeException(Exception)

    Raises when ``DEPOSIT SIZE IS NOT CORRECT !(1/31)`` 

.. py:method::   class WithdrawalCredentialException(Exception)

    Raises when ``INCORRECT withdrawal_credentials`` 

.. py:method::   class GenesisForkException(Exception)

    Raises when ``INCORRECT fork_version`` 

.. py:method::   class NetworkNameException(Exception)

    Raises when ``INCORRECT network_name`` 

.. py:method::   class DepositDataException(Exception)

    Raises when ``CAN NOT VERIFY DEPOSIT DATA`` 
