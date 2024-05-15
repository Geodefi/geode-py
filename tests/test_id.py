from dotenv import dotenv_values
import sys
import os
import pytest
import inspect

sys.path.append(os.getcwd())

try:
    from geodefi import Geode
    from geodefi.classes.id import Id
    from geodefi.exceptions import MaxAttemptError
except ImportError:
    raise


env = dotenv_values(".env")


G = Geode(exec_api=env["EXECUTION_API"], cons_key=env["CONSENSUS_KEY"])


def test_init():
    id = Id(
        G.w3,
        G.network,
        G.Portal,
        id=50016835115526216130031110555486827201953559012021267556883950029143900999178,
    )

    assert id.w3 == G.w3
    assert id.network == G.network
    assert id.portal == G.Portal
    assert (
        id.ID
        == 50016835115526216130031110555486827201953559012021267556883950029143900999178
    )


def test_invalid_arguments():
    # Test case 3: Test with invalid arguments
    # with pytest.raises(TypeError):
    # Trying to initialize the class without providing parameters
    #    id = Id()

    # with pytest.raises(ValueError):
    # Trying to initialize the class with different parameter types

    #    id = Id(1, 2, 3, id="AAAAAA")

    pass


###################################################################
# Init is costly so below test will use this id instance.
###################################################################


id_portal = Id(
    G.w3,
    G.network,
    G.Portal,
    id=50016835115526216130031110555486827201953559012021267556883950029143900999178,
)
id_operator = Id(
    G.w3,
    G.network,
    G.Portal,
    id=50016835115526216130031110555486827201953559012021267556883950029143900999178,
)


def test_str():

    assert (
        str(id_portal)
        == "50016835115526216130031110555486827201953559012021267556883950029143900999178"
    )


def test_readUint():

    # test private variables
    assert id_portal._readUint("initiated") == 0
    assert id_portal._readUint("surplus") == 0
    assert id_portal._readUint("secured") == 0

    # test private variables
    assert id_operator._readUint("released") == 0
    assert id_operator._readUint("totalProposedValidators") == 0
    assert id_operator._readUint("priorFee") == 0


def test_invalid_readUint():

    # test incorrect values
    with pytest.raises(MaxAttemptError):
        id_portal._readUint(1231231)

    with pytest.raises(MaxAttemptError):
        id_portal._readUint(list("maintainer"))


"""
def test_readBytes():

    ## Only use-case of readBytes for now.
    assert id_portal._readBytes(
        "withdrawalCredential") == b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8.\xd5\xecW\x16s\xe6\xb1\x8cK\t,\x9c\xbcJ\xe8lxn'
    assert id_portal._readBytes(
        "withdrawalCredential", isHex= True) == '0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e'


def test_readBytesArray():

    # Only use-case of readBytes for now.
    assert id_portal._readBytesArray(
        "validators", index=0) == b'\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19\'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7"\x8d'

    # Index of empty storage
    assert id_portal._readBytesArray(
        "validators", index=1) == b''


def test_invalid_readBytesArray():

    # Negative index
    with pytest.raises(MaxAttemptError):
        id_portal._readBytesArray(
            "validators", index=-1)




def test_readAddress():

    assert id_portal._readAddress("whitelist") == 0
    assert id_portal._readAddress("withdrawalContract") == 0
    assert id_portal._readAddress("liquidityPool") == 0

"""


def test_NAME():

    assert isinstance(id_portal.NAME, str)  # == "Ice Bear's Pool"
