class PythonVersionError(Exception):
    "Current version is < 3.7 or > 3.10"


class UnknownChainError(Exception):
    "Provided RPC points to an unknown chainId"


class UnexpectedResponseError(Exception):
    "Https call resulted with an error code (non 2xx)"


class HTTPRequestError(Exception):
    "RESPONSE IS NOT CODE 200"


class MaxAttemptError(Exception):
    "MULTIPLE ATTEMPT MADE BUT CALL FAILED"


class DepositSizeError(Exception):
    "DEPOSIT SIZE IS NOT CORRECT !(1/31)"


class WithdrawalCredentialError(Exception):
    "INCORRECT withdrawal_credentials"


class GenesisForkError(Exception):
    "INCORRECT fork_version"


class NetworkNameError(Exception):
    "INCORRECT network_name"


class DepositDataError(Exception):
    "CAN NOT VERIFY DEPOSIT DATA"
