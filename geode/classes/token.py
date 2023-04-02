import logging

from web3 import Web3
from web3.contract.contract import Contract

from geode.globals import Network
from geode.utils import get_contract_abi, get_token_name


class Token(object):
    network: Network
    contract: Contract

    def __init__(self,  w3: Web3, network: Network, **kwarg):
        self.network: Network = network

        token_name = get_token_name(self.network)
        address, abi = get_contract_abi(
            network=self.network, name=token_name)
        self.contract: Contract = w3.eth.contract(
            address=Web3.to_checksum_address(address), abi=abi)
        logging.info(
            f"Token:{token_name}")

    def __getattr__(self, attr):
        return getattr(self.contract, attr)
