class PythonVersionException(Exception):
    "Current version is < 3.7 or > 3.10"


class UnknownChainException(Exception):
    "Provided RPC points to an unknown chainId"


class UnexpectedResponseException(Exception):
    "Https call resulted with an error code (non 2xx)"


class HTTPRequestException(Exception):
    "RESPONSE IS NOT CODE 200"


class MaxAttemptException(Exception):
    "MULTIPLE ATTEMPT MADE BUT CALL FAILED"


class DepositSizeException(Exception):
    "DEPOSIT SIZE IS NOT CORRECT !(1/31)"


class WithdrawalCredentialException(Exception):
    "INCORRECT withdrawal_credentials"


class GenesisForkException(Exception):
    "INCORRECT fork_version"


class NetworkNameException(Exception):
    "INCORRECT network_name"


class DepositDataException(Exception):
    "CAN NOT VERIFY DEPOSIT DATA"
