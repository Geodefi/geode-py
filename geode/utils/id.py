from web3 import Web3

from geode.globals import ID_TYPE
from .solidity import toBytes32
from .crypto import solidity_keccak256


def generateId(name: str, type: ID_TYPE):
    """
    Generates an ID using keccak256 hash function.

    Parameters:
    name (str): The name used to generate the ID.
    type (ID_TYPE): The type of ID to generate.

    Returns:
    int: The generated ID.
    """
    return Web3.to_int(solidity_keccak256(['string', 'uint256'], [name, type]))


def getKey(id: int, key: str):
    """
    Generates a key using keccak256 hash function.

    Parameters:
    id (int): The ID to use in generating the key.
    key (str): The key to generate.

    Returns:
    bytes: The generated key.
    """

    return (solidity_keccak256(['uint256', 'bytes32'], [id, toBytes32(key)]))
