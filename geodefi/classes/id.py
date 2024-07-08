# -*- coding: utf-8 -*-

import logging
import eth_typing as et
from web3 import Web3
from web3.contract import Contract

from geodefi.globals import Network, ID_TYPE
from geodefi.utils import to_bytes32, to_string, multiple_attempt
from geodefi.exceptions import UnexpectedResponseError


class Id:
    """
    A class representing an identifier for some object or entity.

    Attributes:
        w3: A Web3 instance used for interacting with the Ethereum network.
        network: A Network instance representing the Ethereum network to use.
        portal: An Ethereum address of the portal contract.
    """

    w3: Web3
    network: Network
    portal: et.ChecksumAddress

    def __init__(
        self,
        w3: Web3,
        network: Network,
        portal: Contract,
        id_: int,
        type_: int,
    ):
        """
        Initializes a new Id instance with the specified parameters.

        Args:
            w3: A Web3 instance used for interacting with the Ethereum network.
            network: A Network instance representing the Ethereum network to use.
            portal: An Ethereum address of the portal contract.
            id: An integer representing the identifier value.
        """
        self.w3 = w3
        self.network = network
        self.portal = portal
        self.ID = id_
        # TYPE: An enumeration value representing the type of the identifier.
        self.TYPE = type_
        logging.info(f"ID TYPE:{ID_TYPE(self.TYPE).name}:{self.ID}")

    @multiple_attempt
    def _read_uint(self, key: str):
        res = self.portal.functions.readUint(self.ID, to_bytes32(key)).call()
        return res

    @multiple_attempt
    def _read_uint_array(self, key: str, index: int):
        res = self.portal.functions.readUintArray(
            self.ID, to_bytes32(key), index
        ).call()
        return res

    @multiple_attempt
    def _read_bytes(self, key: str, is_string: bool = False, is_hex=False):
        res = self.portal.functions.readBytes(self.ID, to_bytes32(key)).call()

        if isinstance(res, str):
            return res
        elif isinstance(res, bytes):
            if is_string:
                return to_string(res)
            elif is_hex:
                return "0x" + res.hex()
            else:
                return res
        else:
            raise UnexpectedResponseError

    @multiple_attempt
    def _read_bytes_array(
        self, key: str, index: int, is_string: bool = False, is_hex=False
    ):
        res = self.portal.functions.readBytesArray(
            self.ID, to_bytes32(key), index
        ).call()

        if isinstance(res, str):
            return res
        elif isinstance(res, bytes):
            if is_string:
                return to_string(res)
            elif is_hex:
                return res.hex()
            else:
                return res
        else:
            raise UnexpectedResponseError

    @multiple_attempt
    def _read_address(self, key: str):
        res: et.Address = self.portal.functions.readAddress(
            self.ID, to_bytes32(key)
        ).call()
        cs_res: et.ChecksumAddress = Web3.to_checksum_address(res)
        return cs_res

    @multiple_attempt
    def _read_address_array(self, key: str, index: int):
        res: et.Address = self.portal.functions.readAddressArray(
            self.ID, to_bytes32(key), index
        ).call()
        cs_res: et.ChecksumAddress = Web3.to_checksum_address(res)
        return cs_res

    @property
    def NAME(self):
        """
        Returns the name of the object or entity.
        """
        return self._read_bytes("NAME", is_string=True)

    @property
    def CONTROLLER(self):
        """
        Returns the Ethereum address of the controller of the object or entity.
        """
        return self._read_address("CONTROLLER")

    def __str__(self):
        """
        Returns a string representation of this Id instance.
        """
        return str(self.ID)
