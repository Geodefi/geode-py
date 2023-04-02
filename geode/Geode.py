import sys
from web3 import Web3, HTTPProvider
from geode.exceptions import PythonVersionException
from geode.globals import Network
from geode.classes import Portal, Token, Beacon


def check_python_version() -> None:
    '''
    Checks that the python version running is sufficient and exits if not.
    '''
    if sys.version_info < (3, 7):
        raise PythonVersionException
        sys.exit()


class Geode(object):
    def __init__(self, exec_api: str = "",  cons_key: str = "", ** kwargs):
        check_python_version()
        self._set_web3(exec_api)
        if self.network is Network.ethereum or self.network is Network.goerli or self.network is Network.gnosis:
            self._set_beacon(cons_key)

        self._set_Token()
        self._set_Portal()

        # self._set_modules()
        # self._set_configs(kwargs)

    def _set_web3(self,  exec_api: str):
        if exec_api:
            self.w3: Web3 = Web3(HTTPProvider(exec_api))
            self.network: int = Network(self.w3.eth.chain_id)

    def _set_beacon(self,  cons_key: str):
        if cons_key:
            self.Beacon: Beacon = Beacon(
                network=self.network, cons_key=cons_key)

    def _set_Portal(self):
        self.Portal: Portal = Portal(self.w3, self.Beacon)

    def _set_Token(self):
        self.Token: Token = Token(self.w3, self.network)

    # def _set_configs(self, kwargs):
    #     for key, value in kwargs.items():
    #         setattr(config, key, value)
