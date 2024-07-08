# -*- coding: utf-8 -*-

import logging
from web3 import Web3
from web3.contract import Contract

from geodefi.globals import Network
from geodefi.utils import get_contract_abi, to_bytes32, to_string
from geodefi.exceptions import UnknownChainError

from .pool import Pool
from .operator import Operator
from .beacon import Beacon
from .validator import Validator


class Portal:
    """
    Attributes:
        w3: A Web3 instance used for interacting with the Ethereum network.
        network: A Network instance representing the Ethereum network to use.
        portal: An Ethereum address of the portal contract.
    """

    w3: Web3  # Web3 instance used for interacting with the Ethereum network
    network: Network  # Network to which the Portal is connected
    contract: Contract  # Contract instance used for interacting with the Portal contract
    beacon: Beacon  # Beacon instance used for generating deposit keys and signatures
    version: int  # Version of the Portal contract

    def __init__(self, w3: Web3, beacon: Beacon):
        """
        Initializes a new Portal instance.

        Args:
            w3 (Web3): Web3 instance used for interacting with the Ethereum network.
            beacon (Beacon): Beacon instance used for generating deposit keys and signatures.
            kwargs (dict): Optional keyword arguments.
        """
        self._set_web3(w3)  # sets the Web3 instance for the Portal
        if (
            self.network is Network.ethereum
            or self.network is Network.holesky
            or self.network is Network.gnosis
        ):
            self._set_beacon(beacon)
        else:
            raise UnknownChainError

        address, abi = get_contract_abi(
            network=self.network, kind="package", name="Portal"
        )
        self.contract: Contract = w3.eth.contract(
            address=Web3.to_checksum_address(address), abi=abi
        )

        self.version: int = self.functions.getContractVersion().call()
        version_name = self.functions.readBytes(
            self.version, to_bytes32("NAME")
        ).call()
        logging.info(
            f"Portal:{self.network.name} head is on '{to_string(version_name)}'"
        )

    def _set_web3(self, w3: Web3):
        """
        Set the Web3 instance and network based on the chain ID.
        """

        self.w3: Web3 = w3
        self.network: Network = Network(self.w3.eth.chain_id)

    def _set_beacon(self, beacon: Beacon):
        """
        Set the Beacon instance
        """
        self.beacon: Beacon = beacon

    def __getattr__(self, attr):
        return getattr(self.contract, attr)

    def pool(self, id_: int):
        """
        Get the Pool object by id
        """
        return Pool(
            beacon=self.beacon,
            w3=self.w3,
            network=self.network,
            portal=self.contract,
            id_=id_,
        )

    def operator(self, id_: int):
        """
        Get the Opeartor object by id
        """
        return Operator(
            w3=self.w3, network=self.network, portal=self.contract, id_=id_
        )

    def validator(self, pubkey: bytes):
        """
        Get the Opeartor object by id
        """
        return Validator(
            w3=self.w3,
            network=self.network,
            portal=self.contract,
            beacon=self.beacon,
            pk=pubkey,
        )
