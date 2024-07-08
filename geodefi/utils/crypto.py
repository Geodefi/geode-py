from web3 import Web3


def solidity_keccak256(types: list[str], params: list):
    # Calculate Keccak-256 hash of the given solidity types and parameters
    return Web3.solidity_keccak(abi_types=types, values=params)
