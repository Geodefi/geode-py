from web3 import Web3
from Crypto.Hash import keccak as _keccak


def keccak256(x: bytes) -> bytes:
    # Calculate Keccak-256 hash of the input bytes
    return _keccak.new(x).digest()


def solidity_keccak256(types, params):
    # Calculate Keccak-256 hash of the given solidity types and parameters
    return Web3.solidity_keccak(types, params)
