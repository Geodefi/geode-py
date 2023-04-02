import logging
import typing as t
import eth_typing as et
from datetime import datetime

from geode.globals import Network, API_BASE
from geode.utils import httpRequest
from geode.exceptions import UnknownChainException


class Beacon(object):
    # https://beaconcha.in/api/v1/docs/index.html#/
    api_base: str
    api_suffix: str
    last_update: datetime
    beacon_state: t.Dict

    def __init__(self, network: Network, cons_key: str = "", ** kwargs):
        self.api_base = API_BASE[network]
        if self.api_base is None:
            raise UnknownChainException

        self.api_suffix = "?apikey="+cons_key
        logging.info(
            f"Connected to beconcha.in:{self.api_base}")

    @httpRequest
    def get_validator_eth1(self, eth1_address: et.Address):
        url = self.api_base + "validator/eth1/" + eth1_address + self.api_suffix
        return url

    @httpRequest
    def get_validator_withdrawalCredentials(self, wc_or_eth1: str):
        url = self.api_base + "validator/withdrawalCredentials/" + \
            wc_or_eth1 + self.api_suffix
        return url

    @httpRequest
    def get_validator(self, index_or_pk: str):
        url = self.api_base + "validator/" + index_or_pk + self.api_suffix
        return url

    @httpRequest
    def get_validator_balancehistory(self, index_or_pk: str):
        url = self.api_base + index_or_pk + "/balancehistory" + self.api_suffix
        return url

    @httpRequest
    def get_validator_deposits(self, index_or_pk: str):
        url = self.api_base + index_or_pk + "/deposits" + self.api_suffix
        return url

    @httpRequest
    def get_validator_withdrawals(self, index_or_pk: str):
        url = self.api_base + index_or_pk + "/withdrawals" + self.api_suffix
        return url

    @httpRequest
    def get_validators_queue(self):
        url = self.api_base + "validators/queue" + self.api_suffix
        return url

    @httpRequest
    def get_eth1deposit(self, txhash: str):
        url = self.api_base + "eth1deposit/" + txhash + self.api_suffix
        return url

    @httpRequest
    def get_healthz(self):
        url = self.api_base + "healthz"
        return url
