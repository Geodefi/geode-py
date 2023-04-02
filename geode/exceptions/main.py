class PythonVersionException(Exception):
    "VERSION < 3.7"
    pass


class UnknownChainException(Exception):
    "GIVEN NETWORK IS NOT DEFINED"
    pass


class UnexpectedResponseException(Exception):
    "CAN NOT HANDLE RESPONSE"
    pass


class BadRequestException(Exception):
    "RESPONSE IS NOT CODE 200"
    pass


class MaxAttemptException(Exception):
    "MULTIPLE ATTEMPT MADE BUT CALL FAILED"
    pass


class DepositSizeException(Exception):
    "DEPOSIT SIZE IS NOT CORRECT !(1/31)"
    pass


class WithdrawalCredentialException(Exception):
    "INCORRECT withdrawal_credentials"
    pass


class GenesisForkException(Exception):
    "INCORRECT fork_version"
    pass


class NetworkNameException(Exception):
    "INCORRECT network_name"
    pass


class DepositDataException(Exception):
    "CAN NOT VERIFY DEPOSIT DATA"
    pass
