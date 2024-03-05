import typing as t
from geodefi.globals.network import Network


TOKEN_NAMES: t.Dict[Network, str] = {
    Network.ethereum: "gETH",
    Network.holesky: "gETH",
    Network.binance: "gBNB",
    Network.gnosis: "gGNO",
    Network.avalanche: "gAVAX",
}
