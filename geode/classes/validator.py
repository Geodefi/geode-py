import logging
import typing as t
from datetime import datetime, timedelta
from web3 import Web3
from web3.contract import Contract

from geode.globals import Network, VALIDATOR_STATE, REFRESH_RATE
from geode.utils import multipleAttempt

from .beacon import Beacon


class Validator(object):
    w3: Web3
    network: Network
    portal: Contract
    beacon: Beacon

    pubkey: bytes
    portal_state = []
    beacon_state: t.Dict = {}
    last_portal_update: datetime = datetime.now() - timedelta(seconds=REFRESH_RATE+1)
    last_beacon_update: datetime = datetime.now() - timedelta(seconds=REFRESH_RATE+1)

    def __init__(self, w3: Web3,
                 network: Network, portal: Contract, beacon: Beacon, pk: bytes):
        self.w3 = w3
        self.network = network
        self.portal = portal
        self.beacon = beacon
        self.pubkey = "0x" + pk.hex()
        logging.info(
            f"Connected to validator: {self.pubkey}")

    def __str__(self):
        return f"Validator: {self.pubkey}"

    @staticmethod
    @multipleAttempt
    def updatePortal(func):
        def wrap(self):
            if datetime.now() > self.last_portal_update + timedelta(seconds=REFRESH_RATE):
                self.portal_state = self.portal.functions.getValidator(
                    self.pubkey).call()
                self.last_portal_update = datetime.now()
            return func(self)
        return wrap

    @staticmethod
    def updateBeacon(func):
        def wrap(self):
            if datetime.now() > self.last_beacon_update + timedelta(seconds=REFRESH_RATE):
                self.beacon_state = self.beacon.get_validator(
                    self.pubkey)
                self.last_beacon_update = datetime.now()
            return func(self)
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
    def poolIee(self):
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
