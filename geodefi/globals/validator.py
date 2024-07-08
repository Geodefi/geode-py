# -*- coding: utf-8 -*-

from enum import IntEnum


class VALIDATOR_STATE(IntEnum):
    # invalid
    NONE = 0
    # validator is proposed, 1 ETH is sent from Operator to Deposit Contract.
    PROPOSED = 1
    # proposal was approved, operator used pooled funds, 1 ETH is released back to Operator.
    ACTIVE = 2
    # validator is called to be exited.
    EXIT_REQUESTED = 3
    # validator is fully exited.
    EXITED = 4
    # proposal was malicious(alien). Maybe faulty signatures
    # or probably frontrunning (https://bit.ly/3Tkc6UC)
    ALIENATED = 69
