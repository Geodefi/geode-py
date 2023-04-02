import logging
import eth_typing as et
from web3 import Web3
from web3.contract import Contract

from geode.globals import Network, ID_TYPE
from geode.utils import toBytes32, toString, multipleAttempt
from geode.exceptions import UnexpectedResponseException


class Id(object):
    w3: Web3
    network: Network
    portal: et.ChecksumAddress
    ID: int
    TYPE: ID_TYPE(0)

    def __init__(self, w3: Web3, network:
                 Network, portal: Contract, id: int):
        self.w3 = w3
        self.network = network
        self.portal = portal
        self.ID = id
        logging.info(
            f"ID TYPE:{ID_TYPE(self.TYPE).name}:{self.ID}")

    def __str__(self):
        return self.ID

    @multipleAttempt
    def _readUint(self, key: str):
        res = self.portal.functions.readUintForId(
            self.ID, toBytes32(key)).call()
        return res

    @multipleAttempt
    def _readUintArray(self, key: str, index: int):
        res = self.portal.functions.readUintArrayForId(
            self.ID, toBytes32(key), index).call()
        return res

    @multipleAttempt
    def _readBytes(self, key: str, isString: bool = False, isHex=False):
        res = self.portal.functions.readBytesForId(
            self.ID, toBytes32(key)).call()

        if isinstance(res, str):
            return res
        elif isinstance(res, bytes):
            if isString:
                return toString(res)
            elif isHex:
                return "0x" + res.hex()
            else:
                return res
        else:
            raise UnexpectedResponseException

    @multipleAttempt
    def _readBytesArray(self, key: str, index: int, isString: bool = False, isHex=False):
        res = self.portal.functions.readBytesArrayForId(
            self.ID, toBytes32(key), index).call()

        if isinstance(res, str):
            return res
        elif isinstance(res, bytes):
            if isString:
                return toString(res)
            elif isHex:
                return res.hex()
            else:
                return res
        else:
            raise UnexpectedResponseException

    @multipleAttempt
    def _readAddress(self, key: str):
        res: et.Address = self.portal.functions.readAddressForId(
            self.ID, toBytes32(key)).call()
        csRes: et.ChecksumAddress = Web3.to_checksum_address(res)
        return csRes

    @multipleAttempt
    def _readAddressArray(self, key: str, index: int):
        res: et.Address = self.portal.functions.readAddressArrayForId(
            self.ID, toBytes32(key), index).call()
        csRes: et.ChecksumAddress = Web3.to_checksum_address(res)
        return csRes

    @property
    def NAME(self):
        return self._readBytes("NAME", isString=True)

    @property
    def TYPE(self):
        return self._readUint("TYPE")

    @property
    def CONTROLLER(self):
        return self._readAddress("CONTROLLER")
