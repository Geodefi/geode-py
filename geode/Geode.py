import sys
from web3 import Web3, HTTPProvider
from geode.exceptions import PythonVersionException
from geode.globals import Network
from geode.classes import Portal, Token, Beacon


def check_python_version() -> None:
    '''
    Checks that the python version running is sufficient and exits if not.
    '''
    if sys.version_info <= (3, 7):
        raise PythonVersionException
        sys.exit()


class Geode(object):
    def __init__(self, exec_api: str = "", cons_key: str = "", **kwargs):
        # Check if the current version of Python is supported
        check_python_version()

        # Set the Web3 instance with the given execution API
        self._set_web3(exec_api)

        # If the network is Ethereum, Goerli or Gnosis, set the Beacon instance with the given consumer key
        if self.network is Network.ethereum or self.network is Network.goerli or self.network is Network.gnosis:
            self._set_beacon(cons_key)

        # Set the Token instance
        self._set_Token()

        # Set the Portal instance
        self._set_Portal()

        # Set the modules and configurations
        # self._set_modules()
        # self._set_configs(kwargs)

    # Internal method to set the Web3 instance
    def _set_web3(self, exec_api: str):
        if exec_api:
            self.w3: Web3 = Web3(HTTPProvider(exec_api))
            self.network: int = Network(self.w3.eth.chain_id)

    # Internal method to set the Beacon instance
    def _set_beacon(self, cons_key: str):
        if cons_key:
            self.Beacon: Beacon = Beacon(
                network=self.network, cons_key=cons_key)

    # Internal method to set the Portal instance
    def _set_Portal(self):
        self.Portal: Portal = Portal(self.w3, self.Beacon)

    # Internal method to set the Token instance
    def _set_Token(self):
        self.Token: Token = Token(self.w3, self.network)
