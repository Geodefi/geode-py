# -*- coding: utf-8 -*-

from enum import IntEnum


class ID_TYPE(IntEnum):
    NONE = 0
    SENATE = 1
    LIMIT_MIN_USER = 3
    OPERATOR = 4
    POOL = 5
    LIMIT_MAX_USER = 9999
    LIMIT_MIN_PACKAGE = 10000
    PACKAGE_PORTAL = 10001
    PACKAGE_WITHDRAWAL_CONTRACT = 10011
    PACKAGE_LIQUIDITY_POOL = 10021
    LIMIT_MAX_PACKAGE = 19999
    LIMIT_MIN_MIDDLEWARE = 20000
    MIDDLEWARE_GETH = 20011
    LIMIT_MAX_MIDDLEWARE = 2999
