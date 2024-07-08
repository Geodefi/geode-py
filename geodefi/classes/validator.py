# -*- coding: utf-8 -*-

import logging
import typing as t
from datetime import datetime, timedelta
from web3 import Web3
from web3.contract import Contract

from geodefi.globals import Network, VALIDATOR_STATE, REFRESH_RATE
from geodefi.utils import multiple_attempt

from .beacon import Beacon


# This is a static method and a decorator that wraps around another method
# It is used to update the Portal state for the Validator
@multiple_attempt
def update_portal(func):
    # This is the wrapper function that is returned by the decorator.
    # It updates the Portal state if REFRESH_RATE has elapsed
    def wrap(self):
        if datetime.now() > self.last_portal_update + timedelta(
            seconds=REFRESH_RATE
        ):
            # Call the `getValidator()` function on the Portal contract with Validator's pubkey
            # and retrieve its state
            self.portal_state = self.portal.functions.getValidator(
                self.pubkey
            ).call()
            self.last_portal_update = datetime.now()
        # Call the function that was decorated and return its result
        return func(self)

    # Return the wrapper function
    return wrap


# This is a static method and a decorator that wraps around another method
# It is used to update the Beacon chain state for the Validator
@multiple_attempt
def update_beacon(func):
    # This is a decorator function that wraps around the given function.
    # It checks whether the last update to the beacon state is older than REFRESH_RATE seconds.
    def wrap(self):
        if datetime.now() > self.last_beacon_update + timedelta(
            seconds=REFRESH_RATE
        ):
            # If it is, it updates the beacon state by calling get_validator()
            # function of the beacon contract.
            self.beacon_state = self.beacon.beacon_states_validators_id(
                state_id="head", validator_id=self.pubkey
            )
            # It then updates the last_beacon_update timestamp to the current time.
            self.last_beacon_update = datetime.now()
        return func(self)

    # Finally, it returns the wrapped function.
    return wrap


class Validator:
    # Declare instance variables for Validator class
    w3: Web3  # An instance of the Web3 class for interacting with Ethereum blockchain
    network: Network  # The network being validated
    portal: Contract  # The portal contract being used
    beacon: Beacon  # The beacon chain being used

    def __init__(
        self, w3: Web3, network: Network, portal: Contract, beacon: Beacon, pk
    ):
        """
        Initialize the Validator object.

        pk: Public key of the validator, bytes (no 0x prefix) or str (0x prefix)
        """
        self.w3 = w3
        self.network = network
        self.portal = portal
        self.beacon = beacon
        if isinstance(pk, bytes):
            self.pubkey: str = "0x" + pk.hex()
        elif isinstance(pk, str):
            self.pubkey: str = pk

        self.portal_state = []  # A list containing the current portal state
        self.beacon_state: t.Dict = (
            {}
        )  # A dictionary containing the current beacon state
        # update timestamps set on init to be able to catch init state without
        self.last_portal_update: datetime = datetime.now() - timedelta(
            seconds=REFRESH_RATE + 1
        )  # The time of the last portal state update
        self.last_beacon_update: datetime = datetime.now() - timedelta(
            seconds=REFRESH_RATE + 1
        )  # The time of the last beacon state update

        logging.info(f"Connected to the validator: {self.pubkey}")

    def __str__(self):
        return f"Validator Object: {self.pubkey}"

    # Portal Props
    @property
    @update_portal
    def portal_index(self):
        return self.portal_state[1]

    @property
    @update_portal
    def state(self):
        return VALIDATOR_STATE(self.portal_state[0])

    @property
    @update_portal
    def createdAt(self):
        return self.portal_state[2]

    @property
    @update_portal
    def period(self):
        return self.portal_state[3]

    @property
    @update_portal
    def poolId(self):
        return self.portal_state[4]

    @property
    @update_portal
    def operatorId(self):
        return self.portal_state[5]

    @property
    @update_portal
    def poolFee(self):
        return self.portal_state[6]

    @property
    @update_portal
    def operatorFee(self):
        return self.portal_state[7]

    @property
    @update_portal
    def infrastructureFee(self):
        return self.portal_state[8]

    @property
    @update_portal
    def signature31(self):
        return self.portal_state[9]

    @property
    @update_portal
    def __portal__(self):
        keys = [
            "state",
            "index",
            "createdAt",
            "period",
            "poolId",
            "operatorId",
            "poolFee",
            "operatorFee",
            "governanceFee",
            "signature31",
        ]

        return {keys[i]: value for i, value in enumerate(self.portal_state)}

    # Beacon Props

    @property
    @update_beacon
    def beacon_index(self):
        return self.beacon_state["index"]

    @property
    @update_beacon
    def balance(self):
        return self.beacon_state["balance"]

    @property
    @update_beacon
    def beacon_status(self):
        return self.beacon_state["status"]

    @property
    @update_beacon
    def withdrawal_credentials(self):
        return self.beacon_state["validator"]["withdrawal_credentials"]

    @property
    @update_beacon
    def effective_balance(self):
        return self.beacon_state["validator"]["effective_balance"]

    @property
    @update_beacon
    def slashed(self):
        return self.beacon_state["validator"]["slashed"]

    @property
    @update_beacon
    def activation_eligibility_epoch(self):
        return self.beacon_state["validator"]["activation_eligibility_epoch"]

    @property
    @update_beacon
    def exit_epoch(self):
        return self.beacon_state["validator"]["exit_epoch"]

    @property
    @update_beacon
    def withdrawable_epoch(self):
        return self.beacon_state["validator"]["withdrawable_epoch"]

    @property
    @update_beacon
    def __beacon__(self):
        return self.beacon_state
