import typing as t
from geode.globals.network import Network


TOKEN_NAMES: t.Dict[Network, str] = {
    Network.ethereum: "gETH",
    Network.goerli: "gETH",
    Network.binance: "gBNB",
    Network.gnosis: "gGNO",
    Network.avalanche: "gAVAX",
}
