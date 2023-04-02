from os import path
import json
from geode.globals.network import Network

abi_suffix = ".json"


def _get_network_path(network: Network,):
    script_dir = path.dirname(path.dirname(__file__))
    return path.join(path.join(script_dir, 'abis'), network.name)


def _open_abi_file(network: Network, name: str, folder: str):
    abi_path = path.join(
        _get_network_path(network), folder, name+abi_suffix)
    with open(abi_path, "r") as file:
        a = file.read()
    return json.loads(a)


def get_contract_abi(network: Network, name: str):
    abi = _open_abi_file(network, name, folder="contracts")
    return (abi["address"], abi["abi"])


def get_module_abi(network: Network, name: str):
    abi = _open_abi_file(network, name, folder="modules")
    return abi["abi"]
