import logging
from web3 import Web3
from web3.contract import Contract

from geode.globals import Network
from geode.utils import get_contract_abi, toBytes32, toString

from .pool import Pool
from .operator import Operator
from .beacon import Beacon


class Portal(object):
    w3: Web3
    network: Network
    contract: Contract
    Beacon: Beacon
    version: int

    def __init__(self, w3: Web3, beacon: Beacon,  **kwarg):
        self._set_web3(w3)
        if self.network is Network.ethereum or self.network is Network.goerli or self.network is Network.gnosis:
            self._set_beacon(beacon)

        address, abi = get_contract_abi(network=self.network, name="Portal")
        self.contract: Contract = w3.eth.contract(
            address=Web3.to_checksum_address(address), abi=abi)

        self.version: int = self.functions.CONTRACT_VERSION().call()
        version_name = self.functions.readBytesForId(
            self.version, toBytes32("NAME")).call()
        logging.info(
            f"Portal:{self.network.name} head is on '{toString(version_name)}'")

    def _set_web3(self,  w3: Web3):
        self.w3: Web3 = w3
        self.network: Network = Network(self.w3.eth.chain_id)

    def _set_beacon(self,  beacon: Beacon):
        self.Beacon: Beacon = beacon

    def __getattr__(self, attr):
        return getattr(self.contract, attr)

    def pool(self, id: int):
        P: Pool = Pool(beacon=self.Beacon, w3=self.w3, network=self.network,
                       portal=self.contract, id=id)
        return P

    def operator(self,  id: int):
        return Operator(w3=self.w3, network=self.network, portal=self.contract, id=id)
