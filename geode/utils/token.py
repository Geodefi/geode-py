from geode.globals import TOKEN_NAMES
from geode.globals import Network


def get_token_name(network: Network):
    return TOKEN_NAMES[network]
