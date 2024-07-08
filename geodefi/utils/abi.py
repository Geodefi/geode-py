# -*- coding: utf-8 -*-

from os import path
import json
from geodefi.globals.network import Network


def _get_network_path(network: Network):
    # Get the path to the network's ABI folder
    script_dir = path.dirname(path.dirname(__file__))
    return path.join(path.join(script_dir, "abis"), network.name)


def _open_abi_file(network: Network, name: str, folder: str):
    # Load the specified ABI file for the given network and contract/module name
    abi_suffix = ".json"
    abi_path = path.join(_get_network_path(network), folder, name + abi_suffix)
    with open(abi_path, "r", encoding="utf-8") as file:
        a = file.read()
    return json.loads(a)


def get_contract_abi(network: Network, kind: str, name: str):
    # Get the ABI for the specified contract name on the given network.
    # type should be middleware, package or token.
    abi = _open_abi_file(network, name, folder=kind)
    return (abi["address"], abi["abi"])
