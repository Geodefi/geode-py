from web3 import Web3
from Crypto.Hash import keccak as _keccak

from typing import List, Any


def keccak256(x: bytes) -> bytes:
    # Calculate Keccak-256 hash of the input bytes

    return _keccak.new(data=x, digest_bits=256).digest()


def solidity_keccak256(types: List[str], params: List[Any]):
    # Calculate Keccak-256 hash of the given solidity types and parameters
    return Web3.solidity_keccak(types, params)
