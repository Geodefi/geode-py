# -*- coding: utf-8 -*-

import sys
import os
import pytest

sys.path.append(os.getcwd())

from geodefi.utils.crypto import solidity_keccak256


@pytest.mark.parametrize(
    "types, input_data, expected_hash",
    [
        (
            ["uint256"],
            [123],
            b"Ui\x04G\x19\xa1\xec;\x04\xd0\xaf\xa9\xe7\xa51\x0c|\x04s3\x1d\x13\xdc\x9f\xaf\xe1C\xb2\xc4\xe8\x14\x8a",
        ),
        (
            ["bool", "address", "uint256"],
            [True, "0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2", 98765],
            b"2_\xd8\xfc\xb4v\x84\x18,e\xe7\xb6\xce\x9e\xa5\x8e2\xaf1d\xb1\x855\n\x08\xea\x1bX\x0b\xb3\xc0\x00",
        ),
        (
            ["bool", "bool"],
            [True, False],
            b"b\x8b\xf3YgG\xd23\xf1\xe6S3Ep\x00f\xbfE\x8f\xa4\x8d\xae\xda\xf0J{\xe6\xc3\x92\x90$v",
        ),
    ],
)
def test_solidity_keccak256(types, input_data, expected_hash):

    result = solidity_keccak256(types, input_data)
    assert result == expected_hash
