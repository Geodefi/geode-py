from dotenv import dotenv_values
import sys
import os
import pytest
import inspect
import re

from geodefi.utils.merkle import StandartMerkleTree
from geodefi import Geode
from geodefi.classes.operator import Operator


sys.path.append(os.getcwd())


env = dotenv_values(".env")


G = Geode(exec_api=env["EXECUTION_API"], cons_key=env["CONSENSUS_KEY"])
PORTAL = G.Portal

OPERATOR_LIST = [
    114391297015478800753082638170652680401082080549997516459063441314156612391510,
    106440257855610140438147021303249733137151692982873052796064618175630395030085,
]


def test_init():

    myOperator = PORTAL.operator(OPERATOR_LIST[0])
    assert isinstance(myOperator, Operator)

    # == 114391297015478800753082638170652680401082080549997516459063441314156612391510
    assert isinstance(myOperator.ID, int)
    assert myOperator.TYPE == 4
    assert myOperator.network == 5

    assert myOperator.w3 == G.w3

    myOperator2 = PORTAL.operator(
        "114391297015478800753082638170652680401082080549997516459063441314156612391510"
    )
    assert str(myOperator.ID) == myOperator2.ID


myOperator = PORTAL.operator(OPERATOR_LIST[0])


def test_initiated():
    assert myOperator.initiated == 1687433352


def test_totalProposedValidators():
    assert myOperator.totalProposedValidators == 0


def test_totalActiveValidators():
    assert myOperator.totalActiveValidators == 0


def test_feeSwitch():
    assert myOperator.feeSwitch == 0


def test_priorFee():
    assert myOperator.priorFee == 0


def test_fee():
    assert myOperator.fee == 600000000


def test_periodSwitch():
    assert myOperator.periodSwitch == 0


def test_priorPeriod():
    assert myOperator.priorPeriod == 0


def test_validatorPeriod():
    assert myOperator.validatorPeriod == 15552000


def test_wallet():
    assert myOperator.wallet == 0


def test_released():
    assert myOperator.released == 0
