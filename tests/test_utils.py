from dotenv import dotenv_values
import sys
import os
import pytest
import re

from geodefi.utils.id import getKey, generateId
from geodefi.utils.solidity import toBytes
from geodefi.utils.abi import get_module_abi

# ID


@pytest.mark.parametrize(
    "input_str, input_num, expected_output, valid_example",
    [
        # Valid Examples
        (
            "Ice",
            5,
            25684117158848036452621067499879584331094344432967005152759588886290738547975,
            True,
        ),
        (
            "Test",
            0,
            3338633575056120413528041194485442593753618234563731080785778532484242018555,
            True,
        ),
        (
            "Cypher",
            1,
            40152051370629068047466302596126689368494286392338503300166893830613772511565,
            True,
        ),
        (
            "Sonix",
            10,
            88411668354583117024998662858932815776497615934318214720102929601302096204115,
            True,
        ),
        (
            "Crash",
            2,
            32920370699880232445273358357612920189978036342411452933277015652008613329083,
            True,
        ),
        (
            "Python",
            8,
            113619648507393995746416291196618937208347726093758278053809065021754140519795,
            True,
        ),
        (
            "Oranges",
            6,
            18618377329584583019579645282138081976370570556439901182928625776562618568341,
            True,
        ),
        (
            "Pool",
            7,
            34320660771598442116180852498925631406420364039816950455533215223578219351337,
            True,
        ),
        (
            "Vitalik",
            3,
            9036976782520826364234251023176923038226600974938139597527416162006624811135,
            True,
        ),
        (
            "AAAAAA",
            9,
            10207732392703298235020057480322099017154892424369494154725583294064041617851,
            True,
        ),
        # Invalid Examples
        ("Id", "4", 0, False),  # Incorrect input_num
        (5, 11, 0, False),  # Incorrect input_num
        ("B", 2.4, 0, False),  # Incorrect input_num
        ("C", -1, 0, False),  # Incorrect input_num
        (True, 14, 0, False),  # Incorrect input_num
        (b"E", b"15", 0, False),  # Incorrect input_num
    ],
)
def test_generateId(input_str, input_num, expected_output, valid_example):

    if valid_example:
        assert generateId(input_str, input_num) == expected_output
    else:
        with pytest.raises(TypeError):
            generateId(input_str, input_num)


@pytest.mark.parametrize(
    "key, id, expected_output, valid_example",
    [
        # Valid Examples
        (
            "allowance",
            5,
            b"m\x9e\xea\x1e\x1c\xc7<>C\x97p\xcb\x90\x1c\xf8m\nT\x16\xb5\xafo\x10\x0c\x92\x15\xe9\xff\xceo\xc0\x9f",
            True,
        ),
        (
            "type",
            0,
            b"J\x86J\xe2\x1d\xaaj\x01X\xc57\x8c\x1b6Za\xd9\xde\x80\xdc\xf5}ht[\xb3\xbd\xe6\xab\xd9rk",
            True,
        ),
        (
            "maintainer",
            1,
            b"\xe0%\xa6:H\xc5Q=l\xe8\x9f\xcb\xed\xf9\x0f\x15\x18\xd1T\x93\xaa\xa8\xe9\x81d\xf9&+\x85\xe9@\n",
            True,
        ),
        (
            "controller",
            10,
            b"\xeb\x88\n\xc9rw\xb2N\xf7\xf2P\x0bW\xaaf\xaa?\xc1\xe0\xbdl\xde\xebD\x05\xba8,\t\xfe\xc9-",
            True,
        ),
        (
            "wallet",
            2,
            b"[\xf8\xcd\x17\xde\x94A\x84hB\xca\x8aCf\xab\xf6\xd4\xa9\xad[\xd6\xec\xe6\xc6\xca6\x15\x02\x06vH\xfb",
            True,
        ),
        (
            "permission",
            8,
            b"\xe6\x06\xc8\xea\x06\x90v\x87\xd6\xf1\xe3\xb6\xe2\x84'-f\xa7\xbdA}\x85\xc1$G\xc2\xc09\xcb\xf1\xfaK",
            True,
        ),
        (
            "balance",
            6,
            b"\xaa#\xc7#\xf3\x88w4\xa5\x1d\x0c\x0b\x03#\xbbA\xdc\xa0\xfa\xf4\xf2\xbe\xed\xfd\x9aU\x16B\xe4ukF",
            True,
        ),
        (
            "transaction",
            7,
            b"\x1e\x9c\x92\xa3\xea\x91\xca\x187|0\x19\xab(\x1d/\x9c\xf0\x88\xdd\x1d`\xf0\x9f\x8exbu\xb1u\xf9/",
            True,
        ),
        (
            "configuration",
            3,
            b"\xd1\x84\xe6\xf4\xd5\xa2m\x90AE^\xea\xfd\x01.zZ\xddy$B\xf1\x7f\x8c\x19\x1e\xfe\xe5\x01%\xdaD",
            True,
        ),
        (
            "contract",
            9,
            b"\xf2+\x98\xf1v\xe4\n-\xee\x88\x97\x81\xc4L\xbd\xc6!\x93l \xca\xfe_*.\x13\xd4\x99\x13P\xeai",
            True,
        ),
        # Invalid Examples
        ("Id", "4", 0, False),  # Incorrect input_num
        # (5, 11, 0, False),  # Incorrect input_num
        ("B", 2.4, 0, False),  # Incorrect input_num
        ("C", -1, 0, False),  # Incorrect input_num
        # (True, 14, 0, False)  # Incorrect input_num
    ],
)
def test_getKey(key, id, expected_output, valid_example):

    if valid_example:
        print(key, getKey(id, key))
        assert getKey(id, key) == expected_output
    else:
        with pytest.raises(TypeError):
            getKey(id, key)


# SOLIDITY


@pytest.mark.parametrize(
    "key, expected_output",
    [
        ("apple", "0x6170706c65"),
        ("cloud", "0x636c6f7564"),
        ("river", "0x7269766572"),
        ("moon", "0x6d6f6f6e"),
        ("ocean", "0x6f6365616e"),
    ],
)
def test_toBytes(key, expected_output):

    assert toBytes(key) == expected_output


# ABI
