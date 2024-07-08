# -*- coding: utf-8 -*-

import typing as t

from geodefi.globals import ID_TYPE, DEPOSIT_SIZE
from geodefi.utils import get_key


from .id import Id
from .validator import Validator
from .beacon import Beacon


class Pool(Id):
    def __init__(self, beacon: Beacon, *args, **kwargs):
        """
        Initializes a Pool object.

        Parameters:
            beacon: An initialized Beacon object.
            *args: variable length argument list.
            **kwargs: arbitrary keyword arguments.

        Returns:
        None
        """
        # The type of the Pool is 5.
        super().__init__(*args, **kwargs, type_=ID_TYPE(5))
        # The Pool object is associated with a Beacon object.
        self.beacon: Beacon = beacon

    @property
    def initiated(self):
        return self._read_uint("initiated")

    @property
    def maintainer(self):
        return self._read_address("maintainer")

    @property
    def yieldReceiver(self):
        return self._read_address("yieldReceiver")

    @property
    def surplus(self):
        return self._read_uint("surplus")

    @property
    def secured(self):
        return self._read_uint("secured")

    @property
    def middlewares_list(self):
        lenmiddlewares = self.middlewares_len
        ints: t.List = []
        for i in range(lenmiddlewares):
            ints.append(self._read_address_array("middlewares", i))
        return ints

    @property
    def middlewares_len(self):
        return self._read_uint("middlewares")

    def middlewares(self, index):
        return self._read_address_array("middlewares", index)

    @property
    def private(self):
        return self._read_uint("private") == 1

    @property
    def whitelist(self):
        return self._read_address("whitelist")

    @property
    def withdrawalCredential(self):
        return self._read_bytes("withdrawalCredential", is_hex=True)

    @property
    def withdrawalContract(self):
        return self._read_address("withdrawalContract")

    @property
    def liquidityPool(self):
        return self._read_address("liquidityPool")

    @property
    def feeSwitch(self):
        return self._read_uint("feeSwitch")

    @property
    def priorFee(self):
        return self._read_uint("priorFee")

    @property
    def fee(self):
        return self._read_uint("fee")

    @property
    def wallet(self):
        return self._read_uint("wallet")

    @property
    def validatorsList(self):
        lenvalidators = self.validatorsLen
        vals: t.List = []
        for i in range(lenvalidators):
            vals.append(self._read_bytes_array("validators", index=i))
        return vals

    @property
    def validatorsLen(self):
        return self._read_uint("validators")

    @property
    def fallbackOperator(self):
        return self._read_uint("fallbackOperator")

    @property
    def fallbackThreshold(self):
        return self._read_uint("fallbackThreshold")

    def validators(self, index):
        return Validator(
            network=self.network,
            beacon=self.beacon,
            w3=self.w3,
            portal=self.portal,
            pk=self._read_bytes_array("validators", index=index),
        )

    def allowance(self, operator: int):
        return self._read_uint(get_key(id_=operator, key="allowance"))

    def proposedValidators(self, operator: int):
        return self._read_uint(get_key(id_=operator, key="proposedValidators"))

    def activeValidators(self, operator: int):
        return self._read_uint(get_key(id_=operator, key="activeValidators"))

    def alienValidators(self, operator: int):
        return self._read_uint(get_key(id_=operator, key="alienValidators"))
