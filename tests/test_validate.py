from dotenv import dotenv_values
import pytest

from geodefi.utils.bls.validate import (
    SHA256,
    validate_deposit,
    validate_parameters,
)
from geodefi.utils.bls.serialize import (
    DepositData,
    DepositMessage,
    compute_signing_root,
    compute_deposit_fork_data_root,
    compute_deposit_domain,
)
from geodefi.globals.constants import (
    DOMAIN_DEPOSIT,
    ZERO_BYTES32,
)

from eth_typing import (
    BLSPubkey,
    BLSSignature,
)

from py_ecc.bls import G2ProofOfPossession as bls

"""
def test_validate_parameters():
    pass


def test_validate_deposit():
    pass


def test_compute_deposit_domain():
    pass


def test_compute_deposit_fork_data_root():
    pass
"""
"""


def test_compute_deposit_fork_data_root_valid():
    # Test with a valid current_version (4 bytes)
    current_version = b'\x01\x23\x45\x67'
    expected_root = b'\x01\x23\x45\x67' + \
        ZERO_BYTES32[4:]  # Hash tree root of ForkData

    assert compute_deposit_fork_data_root(
        current_version) == b'\xe6"\xc6~\x82\xe5\xe8\x05K@\xf2\x82\x93\x871\xa1\xc0\x06\xe0\x1eZd#\xa6|\x1f\xc7\xce\xb1\xdb\\G'



def test_compute_deposit_fork_data_root_invalid():
    # Test with an invalid current_version (not 4 bytes)
    invalid_version = b'\x01\x23\x45'
    with pytest.raises(ValueError, match="Fork version should be in 4 bytes. Got 3."):
        compute_deposit_fork_data_root(invalid_version)




def test_compute_deposit_fork_data_root_zero_bytes():
    # Test with all zeros in current_version
    current_version = ZERO_BYTES32[:4]
    expected_root = ZERO_BYTES32

    assert compute_deposit_fork_data_root(
        current_version) == b"\xf5\xa5\xfdB\xd1j 0'\x98\xefn\xd3\t\x97\x9bC\x00=# \xd9\xf0\xe8\xea\x981\xa9'Y\xfbK"

"""

# Helper function to create a valid DepositMessage for testing
