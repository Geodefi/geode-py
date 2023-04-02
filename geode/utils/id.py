from web3 import Web3

from geode.globals import ID_TYPE
from .solidity import toBytes32
from .crypto import solidity_keccak256


def generateId(name: str, type: ID_TYPE):
    return Web3.to_int(solidity_keccak256(['string', 'uint256'], [name, type]))


def getKey(id: int, key: str):
    return (solidity_keccak256(['uint256', 'bytes32'], [id, toBytes32(key)]))
