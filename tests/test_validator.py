from dotenv import dotenv_values
import sys
import os
import pytest
import re

from geodefi.utils.merkle import StandartMerkleTree
from geodefi import Geode
from geodefi.classes.validator import Validator


sys.path.append(os.getcwd())


env = dotenv_values(".env")


G = Geode(exec_api=env["EXECUTION_API"], cons_key=env["CONSENSUS_KEY"])
PORTAL = G.Portal

POOL_LIST = [
    50016835115526216130031110555486827201953559012021267556883950029143900999178,
    29228457249232120346521013786824808088246537603535847808963148138747123868265,
]

OPERATOR_LIST = [
    114391297015478800753082638170652680401082080549997516459063441314156612391510,
    106440257855610140438147021303249733137151692982873052796064618175630395030085,
]


def test_init():

    myPool = PORTAL.pool(POOL_LIST[0])
    myVal = myPool.validators(0)

    assert isinstance(myVal, Validator)

    # '0x9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d'
    assert myVal.pubkey == "0x"
    assert myVal.w3 == G.w3
    assert myVal.network == 5
    assert myVal.beacon == G.Beacon
    assert myVal.portal.address == G.Portal.address


# Portal


myPool = PORTAL.pool(POOL_LIST[0])
myVal = myPool.validators(0)


def test_state():
    assert myVal.state == 0


def test_index():
    assert myVal.index == 0


def test_poolId():
    assert myVal.poolId == 0


def test_operatorId():
    assert myVal.operatorId == 0


def test_poolFee():
    assert myVal.poolFee == 0


def test_operatorFee():
    assert myVal.operatorFee == 0


def test_earlyExitFee():
    assert myVal.earlyExitFee == 0


def test_createdAt():
    assert myVal.createdAt == 0


def test_expectedExit():
    assert myVal.expectedExit == 0


def test_signature31():

    # == b'\x94\xc0\x18~I\x0e\xc3\x96r&\xd3\xc3\xce\xbc\xf0\xb0t\xbf\xa0Iq\xe5+\x95t\x8e\x91\x93?\x93\xfc?\x93g}\x94tM\xf5 \x89|\x99\xd3sn\xd1\xdb\x08\xa8!i\x813\xc2b\xb3SdB\x95Y\xa1\xb0z\xc4\x85`\xd2z.g\x88Dq\xf8R/g\xae\nB\xfa\xaa\xee!~\x9c@\xe0\\\xd91(\xad\xdb'
    assert isinstance(myVal.signature31, bytes)
    # == '94c0187e490ec3967226d3c3cebcf0b074bfa04971e52b95748e91933f93fc3f93677d94744df520897c99d3736ed1db08a821698133c262b35364429559a1b07ac48560d27a2e67884471f8522f67ae0a42faaaee217e9c40e05cd93128addb'
    # assert int(myVal.signature31.hex(), 16)


def test_str():
    # 9326f6c07f8abd082ef82b19279cbba7616b0395fb947d50cd2d5fef303dd613abe31087077a67faa477c0631cc7228d'
    assert str(myVal) == "Validator Object: 0x"


# BEACON


"""
def test_activationEligibilityEpoch():
    assert myVal.activationEligibilityEpoch == 0


def test_activationEpoch():
    assert myVal.activationEpoch == 0


def test_balance():
    assert myVal.balance == 0


def test_effectiveBalance():
    assert myVal.effectiveBalance == 0


def test_exitepoch():
    assert myVal.exitepoch == 0


def test_lastAttestationSlot():
    assert myVal.lastAttestationSlot == 0


def test_slashed():
    assert myVal.slashed == 0


def test_status():
    assert myVal.status == 0


def test_validatorIndex():
    assert myVal.validatorIndex == 0


def test_withdrawableEpoch():
    assert myVal.withdrawableEpoch == 0


def test_withdrawalCredentials():
    assert myVal.withdrawalCredentials == 0


def test_totalWithdrawals():
    assert myVal.totalWithdrawals == 0
"""
