# -*- coding: utf-8 -*-


class PythonVersionError(Exception):
    "Python version is not supported."


class UnknownChainError(Exception):
    "Provided RPC points to an unknown chainId"


class UnexpectedResponseError(Exception):
    "Https call resulted with an error code (non 2xx)"


class HTTPRequestError(Exception):
    "Response code is not 200"


class MaxAttemptError(Exception):
    "Multiple attempt made but all failed"


class UnknownApiError(Exception):
    "Provided API endpoint is not recognized"
