# -*- coding: utf-8 -*-

import os

# Solidity
ZERO_BYTES = b""
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
ZERO_BYTES32 = b"\x00" * 32

# 100% = 1e10 on Geode's contracts
PERCENTAGE_DENOMINATOR = 10_000_000_000

# 1 ether = 1e18 wei
ETHER_DENOMINATOR: int = 1_000_000_000_000_000_000

# beacon has 9 decimal points, while eth has 18
ETH2GWEI = 1_000_000_000

# 1 execution ether = 1 beacon ether * 1e9
BEACON_DENOMINATOR: int = 1_000_000_000

# Validator Constants
DEPOSIT_CLI_VERSION = "2.4.0"
WORD_LIST_PATH = os.path.join("geode", "utils", "bls")

# Execution-spec constants taken from:
# https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md
DOMAIN_DEPOSIT = bytes.fromhex("03000000")
BLS_WITHDRAWAL_PREFIX = bytes.fromhex("00")
ETH1_ADDRESS_WITHDRAWAL_PREFIX = bytes.fromhex("01")

MIN_DEPOSIT_AMOUNT = 2**0 * ETHER_DENOMINATOR
MAX_DEPOSIT_AMOUNT = 2**5 * ETHER_DENOMINATOR

# Network
REFRESH_RATE = 60  # in seconds
MAX_ATTEMPT = 60
ATTEMPT_RATE = 0.1  # in seconds
