from web3 import Web3
from Crypto.Hash import keccak as _keccak


def keccak256(x: bytes) -> bytes:
    return _keccak.new(x).digest()


def solidity_keccak256(types, params):
    return Web3.solidity_keccak(types, params)
