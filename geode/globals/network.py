from enum import IntEnum
import typing as t


class Network(IntEnum):
    ethereum = 1
    holesky = 17000
    binance = 56
    gnosis = 100
    avalanche = 43114


API_BASE: t.Dict[Network, bytes] = {
    Network.ethereum: "https://beaconcha.in/api/v1",
    Network.holesky: "https://goerli.beaconcha.in/api/v1/",
    Network.binance: None,
    Network.gnosis: None,
    Network.avalanche: None,
}
