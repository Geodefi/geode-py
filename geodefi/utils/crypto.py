# -*- coding: utf-8 -*-

from typing import List, Any
from web3 import Web3


def keccak256(x: bytes) -> bytes:
    # Calculate Keccak-256 hash of the input bytes
    return Web3.keccak(x)


def solidity_keccak256(types: List[str], params: List[Any]):
    # Calculate Keccak-256 hash of the given solidity types and parameters
    return Web3.solidity_keccak(abi_types=types, values=params)
