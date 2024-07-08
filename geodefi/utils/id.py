# -*- coding: utf-8 -*-

from web3 import Web3
from eth_abi import encode

from geodefi.globals import ID_TYPE

from .solidity import to_bytes32
from .crypto import solidity_keccak256, keccak256


def generate_id(name: str, type_: ID_TYPE):
    """
    Generates an ID using keccak256 hash function.

    Parameters:
    name (str): The name used to generate the ID.
    type (ID_TYPE): The type of ID to generate.

    Returns:
    int: The generated ID.
    """
    return Web3.to_int(keccak256(encode(["string", "uint256"], [name, type_])))


def get_key(id_: int, key: str):
    """
    Generates a key using keccak256 hash function.

    Parameters:
    id (int): The ID to use in generating the key.
    key (str): The key to generate.

    Returns:
    bytes: The generated key.
    """

    return solidity_keccak256(["uint256", "bytes32"], [id_, to_bytes32(key)])
