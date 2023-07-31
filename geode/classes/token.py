import logging

from web3 import Web3
from web3.contract import Contract

from geode.globals import Network
from geode.utils import get_contract_abi, get_token_name


class Token(object):
    network: Network
    contract: Contract

    def __init__(self,  w3: Web3, network: Network, **kwarg):
        # Set the network of the token
        self.network: Network = network

        # Get the name, address and ABI of the token contract
        token_name = get_token_name(self.network)
        address, abi = get_contract_abi(network=self.network, name=token_name)

        # Instantiate the contract using Web3 instance, address and ABI
        self.contract: Contract = w3.eth.contract(
            address=Web3.toChecksumAddress(address), abi=abi)

        # Log the token name
        logging.info(f"Token:{token_name}")

    def __getattr__(self, attr):
        return getattr(self.contract, attr)
