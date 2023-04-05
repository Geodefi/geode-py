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

    def __init__(self, network: Network, cons_key: str = "", **kwargs):
        """
        Initializes a new instance of the class.

        Args:
            network: A `Network` object representing the blockchain network to connect to.
            cons_key: A string representing the API key to use for authenticated requests.
            **kwargs: Any additional keyword arguments to pass to the initializer.

        Raises:
            UnknownChainException: If the specified `network` is not recognized.
        """
        # Get the API base URL for the specified `network`
        self.api_base = API_BASE[network]

        # If the API base URL is not found, raise an exception
        if self.api_base is None:
            raise UnknownChainException

        # Set the `api_suffix` variable to include the API key (if provided)
        self.api_suffix = "?apikey=" + cons_key

        # Log a message indicating that the class instance is connected to the API base
        logging.info(f"Connected to beconcha.in:{self.api_base}")

    # Retrieves the validator data for the specified Ethereum 1.0 address.

    @httpRequest
    def get_validator_eth1(self, eth1_address: et.Address):
        url = self.api_base + "validator/eth1/" + eth1_address + self.api_suffix
        return url

    # Retrieves the validator data for the specified withdrawal credentials or Ethereum 1.0 address.
    @httpRequest
    def get_validator_withdrawalCredentials(self, wc_or_eth1: str):
        url = self.api_base + "validator/withdrawalCredentials/" + \
            wc_or_eth1 + self.api_suffix
        return url

    # Retrieves the validator data for the specified Ethereum 1.0 address.
    @httpRequest
    def get_validator(self, index_or_pk: str):
        url = self.api_base + "validator/" + index_or_pk + self.api_suffix
        return url

    # Retrieves the validator's balance history data for the specified public key or index.
    @httpRequest
    def get_validator_balancehistory(self, index_or_pk: str):
        url = self.api_base + index_or_pk + "/balancehistory" + self.api_suffix
        return url

    # Retrieves the validator's deposit history data for the specified public key or index.
    @httpRequest
    def get_validator_deposits(self, index_or_pk: str):
        url = self.api_base + index_or_pk + "/deposits" + self.api_suffix
        return url

    # Retrieves the validator's withdrawals history data for the specified public key or index.
    @httpRequest
    def get_validator_withdrawals(self, index_or_pk: str):
        url = self.api_base + index_or_pk + "/withdrawals" + self.api_suffix
        return url

    # Retrieves the validator's queue history data for the specified public key or index.
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
