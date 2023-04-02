from enum import IntEnum


class VALIDATOR_STATE(IntEnum):
    NONE = 0
    PROPOSED = 1
    ACTIVE = 2
    EXITED = 3
    ALIEN = 69
