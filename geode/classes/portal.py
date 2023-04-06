import logging
from web3 import Web3
from web3.contract import Contract

from geode.globals import Network
from geode.utils import get_contract_abi, toBytes32, toString

from .pool import Pool
from .operator import Operator
from .beacon import Beacon


class Portal:
    w3: Web3  # Web3 instance used for interacting with the Ethereum network
    network: Network  # Network to which the Portal is connected
    contract: Contract  # Contract instance used for interacting with the Portal contract
    Beacon: Beacon  # Beacon instance used for generating deposit keys and signatures
    version: int  # Version of the Portal contract

    def __init__(self, w3: Web3, beacon: Beacon, **kwargs):
        """
        Initializes a new Portal instance.

        Args:
            w3 (Web3): Web3 instance used for interacting with the Ethereum network.
            beacon (Beacon): Beacon instance used for generating deposit keys and signatures.
            kwargs (dict): Optional keyword arguments.
        """
        self._set_web3(w3)  # sets the Web3 instance for the Portal
        if self.network is Network.ethereum or self.network is Network.goerli or self.network is Network.gnosis:
            self._set_beacon(beacon)

        address, abi = get_contract_abi(network=self.network, name="Portal")
        self.contract: Contract = w3.eth.contract(
            address=Web3.toChecksumAddress(address), abi=abi)

        self.version: int = self.functions.CONTRACT_VERSION().call()
        version_name = self.functions.readBytesForId(
            self.version, toBytes32("NAME")).call()
        logging.info(
            f"Portal:{self.network.name} head is on '{toString(version_name)}'")

    def _set_web3(self,  w3: Web3):
        """
        Set the Web3 instance and network based on the chain ID.
        """

        self.w3: Web3 = w3
        self.network: Network = Network(self.w3.eth.chain_id)

    def _set_beacon(self,  beacon: Beacon):
        """
        Set the Beacon instance
        """
        self.Beacon: Beacon = beacon

    def __getattr__(self, attr):
        return getattr(self.contract, attr)

    def pool(self, id: int):
        """
        Get the Pool object by id
        """
        return Pool(beacon=self.Beacon, w3=self.w3, network=self.network,
                    portal=self.contract, id=id)

    def operator(self,  id: int):
        """
        Get the Opeartor object by id
        """
        return Operator(w3=self.w3, network=self.network, portal=self.contract, id=id)
