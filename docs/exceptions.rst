.. _exceptions:


Exceptions
===============

.. py:exception:: PythonVersionError

    Raises whenPython ``Current version is < 3.7 or > 3.10`` 

.. py:exception:: UnknownChainError

    Raises when ``Provided RPC points to an unknown chainId`` 

.. py:exception:: UnexpectedResponseError

    Raises when ``Https call resulted with an error code (non 2xx)`` 

.. py:exception:: HTTPRequestError

    Raises when ``RESPONSE IS NOT CODE 200`` 

.. py:exception:: MaxAttemptError

    Raises when ``MULTIPLE ATTEMPT MADE BUT CALL FAILED`` 