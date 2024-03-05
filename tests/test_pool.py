from dotenv import dotenv_values
import sys
import os
import pytest
import inspect
import re

from geodefi.utils.merkle import StandartMerkleTree
from geodefi import Geode
from geodefi.classes.validator import Validator


sys.path.append(os.getcwd())


env = dotenv_values(".env")


G = Geode(exec_api=env["EXECUTION_API"], cons_key=env["CONSENSUS_KEY"])
PORTAL = G.Portal


POOL_LIST = [
    "50016835115526216130031110555486827201953559012021267556883950029143900999178",
    "29228457249232120346521013786824808088246537603535847808963148138747123868265",
    "13237608342217427718393841084329878006268509356659527629195599913782184459845",
    "70609728262553005376169614685188798579261852324203356795003385284436695946570",
    "84581558291237928112291510488374176467358729712668559583760486858349467929555",
]


def test_init():

    myPool = PORTAL.pool(POOL_LIST[0])

    # == 50016835115526216130031110555486827201953559012021267556883950029143900999178
    assert isinstance(myPool.ID, int)
    assert myPool.TYPE == 5
    assert myPool.network == 5

    assert myPool.Beacon == G.Beacon
    assert myPool.w3 == G.w3

    myPool2 = PORTAL.pool(
        50016835115526216130031110555486827201953559012021267556883950029143900999178
    )
    assert myPool.ID == myPool2.ID


def test_invalid_init():

    # with pytest.raises(ValueError, match=re.escape("invalid literal for int() with base 10: 'string'")):
    #    PORTAL.pool('string')

    with pytest.raises(
        TypeError,
        match=re.escape(
            "int() argument must be a string, a bytes-like object or a real number, not 'list'"
        ),
    ):
        PORTAL.pool(["LIST", "LII"])


# WARNING: readAddress is not working....

# assert myPool.maintainer == 0
# assert myPool.middlewaresList == 0
# assert myPool.whitelist == 0
# assert myPool.withdrawalContract == 0
# assert myPool.liquidityPool == 0


def test_allowance():
    myPool = PORTAL.pool(POOL_LIST[0])

    operatorID = 114391297015478800753082638170652680401082080549997516459063441314156612391510
    # 114391297015478800753082638170652680401082080549997516459063441314156612391510

    assert myPool.allowance(operatorID) == 10

    assert myPool.allowance(0) == 0

    assert (
        myPool.allowance(
            106440257855610140438147021303249733137151692982873052796064618175630395030085
        )
        == 0
    )

    with pytest.raises(
        TypeError,
        match=re.escape("The following abi value is not a 'uint256': -1"),
    ):
        myPool.allowance(-1) == 0

    with pytest.raises(
        TypeError,
        match=re.escape("The following abi value is not a 'uint256': 11.4"),
    ):
        myPool.allowance(11.4) == 0


def test_proposedValidators():
    myPool = PORTAL.pool(POOL_LIST[0])

    operatorID = 114391297015478800753082638170652680401082080549997516459063441314156612391510
    # 114391297015478800753082638170652680401082080549997516459063441314156612391510

    assert myPool.proposedValidators(operatorID) == 0

    assert (
        myPool.proposedValidators(
            106440257855610140438147021303249733137151692982873052796064618175630395030085
        )
        == 0
    )

    with pytest.raises(
        TypeError,
        match=re.escape("The following abi value is not a 'uint256': -1"),
    ):
        myPool.proposedValidators(-1) == 0

    with pytest.raises(
        TypeError,
        match=re.escape("The following abi value is not a 'uint256': 11.4"),
    ):
        myPool.proposedValidators(11.4) == 0


def test_activeValidators():
    myPool = PORTAL.pool(POOL_LIST[0])

    operatorID = 114391297015478800753082638170652680401082080549997516459063441314156612391510
    # 114391297015478800753082638170652680401082080549997516459063441314156612391510

    assert myPool.activeValidators(operatorID) == 1

    assert (
        myPool.activeValidators(
            106440257855610140438147021303249733137151692982873052796064618175630395030085
        )
        == 0
    )

    with pytest.raises(
        TypeError,
        match=re.escape("The following abi value is not a 'uint256': -1"),
    ):
        myPool.activeValidators(-1) == 0

    with pytest.raises(
        TypeError,
        match=re.escape("The following abi value is not a 'uint256': 11.4"),
    ):
        myPool.activeValidators(11.4) == 0


# WARNING: readAddress does not work...

"""
def test_middlewares():
    myPool = PORTAL.pool(POOL_LIST[0])

    print(myPool.middlewares(0))
    print(myPool.middlewares(1))
    print(myPool.middlewares(-1))
"""


def test_validators():

    myPool = PORTAL.pool(POOL_LIST[0])

    # Call the validators method
    myVal = myPool.validators(0)

    # Check if the returned object is an instance of Validator
    assert isinstance(myVal, Validator)

    # Check if the attributes of the Validator object match the expected values
    assert myVal.network == G.network
    assert myVal.beacon == G.Beacon
    assert myVal.w3 == G.w3
    assert myVal.poolId == int(POOL_LIST[0])


def test_prepareProposeStake():
    pass


def test_prepareBeaconStake():
    pass


myPool = PORTAL.pool(POOL_LIST[0])


def test_initiated():
    assert myPool.initiated == 1677379164


def test_surplus():
    assert myPool.surplus == 0


def test_secured():
    assert myPool.secured == 0


def test_middlewaresLen():
    assert myPool.middlewaresLen == 1


def test_private():
    assert myPool.private == 0


def test_withdrawalCredential():
    assert (
        myPool.withdrawalCredential
        == "0x010000000000000000000000c82ed5ec571673e6b18c4b092c9cbc4ae86c786e"
    )


def test_feeSwitch():
    assert myPool.feeSwitch == 0


def test_priorFee():
    assert myPool.priorFee == 0


def test_fee():
    assert myPool.fee == 500000000


def test_wallet():
    assert myPool.wallet == 0


def test_validatorsLen():
    assert myPool.validatorsLen == 1


def test_validatorsList():

    assert myPool.validatorsList == [
        b"\x93&\xf6\xc0\x7f\x8a\xbd\x08.\xf8+\x19'\x9c\xbb\xa7ak\x03\x95\xfb\x94}P\xcd-_\xef0=\xd6\x13\xab\xe3\x10\x87\x07zg\xfa\xa4w\xc0c\x1c\xc7\"\x8d"
    ]
