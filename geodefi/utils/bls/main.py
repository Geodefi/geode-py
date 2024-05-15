from os import path
import json
import typing as t
from geodefi.globals import (
    Network,
    DEPOSIT_SIZE,
    DEPOSIT_NETWORK_NAME,
    GENESIS_FORK_VERSION,
)
from geodefi.exceptions import (
    DepositSizeError,
    WithdrawalCredentialError,
    GenesisForkError,
    NetworkNameError,
    DepositDataError,
)

from .validate import validate_deposit


def resource_path(relative_path: str) -> str:
    """
    Get the absolute path to a resource in a manner friendly to PyInstaller.
    PyInstaller creates a temp folder and stores path in _MEIPASS which this function swaps
    into a resource path so it is available both when building binaries and running natively.
    """
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = path.abspath(".")
    return path.join(base_path, relative_path)


def _get_deposit_data(deposit_data_path: str):
    file_path = resource_path(deposit_data_path)
    with open(file_path, "r") as file:
        a = file.read()
    return json.loads(a)


def validate_deposit_data_file(
    deposit_data_path: str,
    amount: DEPOSIT_SIZE,
    credential: str,
    network: Network,
):
    deposit_data: t.List[t.Dict] = _get_deposit_data(deposit_data_path)
    for deposit in deposit_data:
        if deposit["amount"] != amount.value:
            raise DepositSizeError
        if deposit["withdrawal_credentials"] != credential:
            raise WithdrawalCredentialError
        if (
            bytes.fromhex(deposit["fork_version"])
            != GENESIS_FORK_VERSION[network.value]
        ):
            raise GenesisForkError
        if deposit["network_name"] != DEPOSIT_NETWORK_NAME[network.value]:
            raise NetworkNameError
        if not validate_deposit(deposit):
            raise DepositDataError
    return deposit_data
