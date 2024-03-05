import sys
from web3 import Web3, HTTPProvider, WebsocketProvider
from geodefi.exceptions import PythonVersionException, UnknownChainException
from geodefi.globals import Network
from geodefi.classes import Portal, Token, Beacon


def check_python_version() -> None:
    """
    Checks that the python version running is sufficient and exits if not.
    """
    if sys.version_info <= (3, 7) and sys.version_info >= (3, 10):
        raise PythonVersionException
        sys.exit()


class Geode:
    def __init__(self, exec_api: str = "", cons_api: str = ""):
        # Check if the current version of Python is supported
        check_python_version()

        # Set the Web3 instance with the given execution API
        self._set_web3(exec_api)

        # If the network is Ethereum, Holesky or Gnosis, set the Beacon instance with the given consumer key
        if (
            self.network is Network.ethereum
            or self.network is Network.holesky
            or self.network is Network.gnosis
        ):
            self._set_beacon(cons_api)
        else:
            raise UnknownChainException

        # Set the Token instance
        self._set_token()

        # Set the Portal instance
        self._set_portal()

    # Internal method to set the Web3 instance
    def _set_web3(self, exec_api: str):
        if exec_api:
            if exec_api.startswith("https"):
                self.w3: Web3 = Web3(HTTPProvider(exec_api))
            elif exec_api.startswith("wss"):
                self.w3: Web3 = Web3(WebsocketProvider(exec_api))
            else:
                # TODO raise if not provided
                pass

            self.network: int = Network(self.w3.eth.chain_id)

    # Internal method to set the Beacon instance
    def _set_beacon(self, cons_api: str):
        if cons_api:
            self.beacon: Beacon = Beacon(
                network=self.network, cons_api=cons_api
            )
        # TODO raise if not provided

    # Internal method to set the Portal instance
    def _set_portal(self):
        self.portal: Portal = Portal(self.w3, self.beacon)

    # Internal method to set the Token instance
    def _set_token(self):
        self.token: Token = Token(self.w3, self.network)
