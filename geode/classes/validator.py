import logging
import typing as t
from datetime import datetime, timedelta
from web3 import Web3
from web3.contract import Contract

from geode.globals import Network, VALIDATOR_STATE, REFRESH_RATE
from geode.utils import multipleAttempt

from .beacon import Beacon


class Validator(object):
    # Declare instance variables for Validator class
    w3: Web3  # An instance of the Web3 class for interacting with Ethereum blockchain
    network: Network  # The network being validated
    portal: Contract  # The portal contract being used
    beacon: Beacon  # The beacon chain being used

    pubkey: bytes  # Public key of the validator
    portal_state = []  # A list containing the current portal state
    beacon_state: t.Dict = {}  # A dictionary containing the current beacon state
    # update timestamps set on init to be able to catch init state without
    last_portal_update: datetime = datetime.now() - timedelta(seconds=REFRESH_RATE +
                                                              1)  # The time of the last portal state update
    last_beacon_update: datetime = datetime.now() - timedelta(seconds=REFRESH_RATE +
                                                              1)  # The time of the last beacon state update

    def __init__(self, w3: Web3,
                 network: Network, portal: Contract, beacon: Beacon, pk: bytes):
        """
        Initialize the Validator object.
        """
        self.w3 = w3
        self.network = network
        self.portal = portal
        self.beacon = beacon
        self.pubkey = "0x" + pk.hex()
        logging.info(
            f"Connected to validator: {self.pubkey}")

    def __str__(self):
        return f"Validator Object: {self.pubkey}"

    # This is a static method and a decorator that wraps around another method
    # It is used to update the Portal state for the Validator
    @staticmethod
    @multipleAttempt
    def updatePortal(func):
        # This is the wrapper function that is returned by the decorator.
        # It updates the Portal state if REFRESH_RATE has elapsed
        def wrap(self):
            if datetime.now() > self.last_portal_update + timedelta(seconds=REFRESH_RATE):
                # Call the `getValidator()` function on the Portal contract with Validator's pubkey
                # and retrieve its state
                self.portal_state = self.portal.functions.getValidator(
                    self.pubkey).call()
                self.last_portal_update = datetime.now()
            # Call the function that was decorated and return its result
            return func(self)
        # Return the wrapper function
        return wrap

    @staticmethod
    def updateBeacon(func):
        # This is a decorator function that wraps around the given function.
        # It checks whether the last update to the beacon state is older than REFRESH_RATE seconds.
        def wrap(self):
            if datetime.now() > self.last_beacon_update + timedelta(seconds=REFRESH_RATE):
                # If it is, it updates the beacon state by calling get_validator() function of the beacon contract.
                self.beacon_state = self.beacon.get_validator(
                    self.pubkey)
                # It then updates the last_beacon_update timestamp to the current time.
                self.last_beacon_update = datetime.now()
            return func(self)

        # Finally, it returns the wrapped function.
        return wrap

    # Portal Props
    @property
    @updatePortal
    def state(self):
        return VALIDATOR_STATE(self.portal_state[0])

    @property
    @updatePortal
    def index(self):
        return self.portal_state[1]

    @property
    @updatePortal
    def poolId(self):
        return self.portal_state[2]

    @property
    @updatePortal
    def operatorId(self):
        return self.portal_state[3]

    @property
    @updatePortal
    def poolFee(self):
        return self.portal_state[4]

    @property
    @updatePortal
    def operatorFee(self):
        return self.portal_state[5]

    @property
    @updatePortal
    def earlyExitFee(self):
        return self.portal_state[6]

    @property
    @updatePortal
    def createdAt(self):
        return self.portal_state[7]

    @property
    @updatePortal
    def expectedExit(self):
        return self.portal_state[8]

    @property
    @updatePortal
    def signature31(self):
        return self.portal_state[9]

    # Beacon Props
    @property
    @updateBeacon
    def activationEligibilityEpoch(self):
        return self.beacon_state["activationeligibilityepoch"]

    @property
    @updateBeacon
    def activationEpoch(self):
        return self.beacon_state["activationepoch"]

    @property
    @updateBeacon
    def balance(self):
        return self.beacon_state["balance"]

    @property
    @updateBeacon
    def effectiveBalance(self):
        return self.beacon_state["effectivebalance"]

    @property
    @updateBeacon
    def exitepoch(self):
        return self.beacon_state["exitepoch"]

    @property
    @updateBeacon
    def lastAttestationSlot(self):
        return self.beacon_state["lastattestationslot"]

    @property
    @updateBeacon
    def slashed(self):
        return self.beacon_state["slashed"]

    @property
    @updateBeacon
    def status(self):
        return self.beacon_state["status"]

    @property
    @updateBeacon
    def validatorIndex(self):
        return self.beacon_state["validatorindex"]

    @property
    @updateBeacon
    def withdrawableEpoch(self):
        return self.beacon_state["withdrawableepoch"]

    @property
    @updateBeacon
    def withdrawalCredentials(self):
        return self.beacon_state["withdrawalcredentials"]

    @property
    @updateBeacon
    def totalWithdrawals(self):
        return self.beacon_state["total_withdrawals"]
