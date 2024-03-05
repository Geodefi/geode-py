import sys
import os
import pytest

sys.path.append(os.getcwd())

try:
    import geodefi
    from geodefi.utils.crypto import keccak256, solidity_keccak256
except ImportError:
    raise


@pytest.mark.parametrize(
    "input_data, expected_hash",
    [
        (
            b"Hello, World!",
            b"\xac\xaf2\x89\xd7\xb6\x01\xcb\xd1\x14\xfb6\xc4\xd2\x9c\x85\xbb\xfd^\x13?\x14\xcb5\\?\xd8\xd9\x93g\x96O",
        ),
        (
            b"12345",
            b"\x18A\xd6S\xf9\xc4\xed\xda\x9df\xa7\xe7s{9v=k\xd4\x0fV\x9a>\xc6\x85\x9d3\x05\xb7#\x10\xe6",
        ),
        (
            b"",
            b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';{\xfa\xd8\x04]\x85\xa4p",
        ),
    ],
)
def test_keccak256(input_data, expected_hash):

    result = keccak256(input_data)
    assert result == expected_hash


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
