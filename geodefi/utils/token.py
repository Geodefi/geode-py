# -*- coding: utf-8 -*-

from geodefi.globals import TOKEN_NAMES
from geodefi.globals import Network


def get_token_name(network: Network):
    return TOKEN_NAMES[network]
