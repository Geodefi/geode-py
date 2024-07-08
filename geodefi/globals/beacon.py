# -*- coding: utf-8 -*-

from enum import IntEnum
import typing as t

from .network import Network


class DEPOSIT_SIZE(IntEnum):
    """
    proposeStake: takes 1 ether from the operator internal wallet
    beaconStake: takes 31 ether from pool & reimburses the operator's 1 ether
    """

    PROPOSAL = 1_000_000_000
    STAKE = 31_000_000_000


DEPOSIT_NETWORK_NAME: t.Dict[Network, bytes] = {
    Network.ethereum: "mainnet",
    Network.holesky: "holesky",
    Network.binance: None,
    Network.gnosis: "gnosis",
    Network.avalanche: None,
}

GENESIS_FORK_VERSION: t.Dict[Network, bytes] = {
    Network.ethereum: bytes.fromhex("00000000"),
    Network.holesky: bytes.fromhex("01017000"),
    Network.binance: None,
    Network.gnosis: bytes.fromhex("00000064"),
    Network.avalanche: None,
}
