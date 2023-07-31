from os import path
import json
import typing as t
from geode.globals import Network, DEPOSIT_SIZE, DEPOSIT_NETWORK_NAME, GENESIS_FORK_VERSION
from geode.exceptions import (
    DepositSizeException,
    WithdrawalCredentialException,
    GenesisForkException,
    NetworkNameException,
    DepositDataException)

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


def validate_deposit_data_file(deposit_data_path: str,
                               amount: DEPOSIT_SIZE,
                               credential: str,
                               network: Network):
    deposit_data: t.List[t.Dict] = _get_deposit_data(deposit_data_path)
    for deposit in deposit_data:
        if deposit["amount"] != amount.value:
            raise DepositSizeException
        if deposit["withdrawal_credentials"] != credential:
            raise WithdrawalCredentialException
        if bytes.fromhex(deposit["fork_version"]) != GENESIS_FORK_VERSION[network.value]:
            raise GenesisForkException
        if deposit["network_name"] != DEPOSIT_NETWORK_NAME[network.value]:
            raise NetworkNameException
        if not validate_deposit(deposit):
            raise DepositDataException
    return deposit_data
