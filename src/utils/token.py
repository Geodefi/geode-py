# -*- coding: utf-8 -*-

from src.globals import TOKEN_NAMES
from src.globals import Network


def get_token_name(network: Network):
    return TOKEN_NAMES[network]
