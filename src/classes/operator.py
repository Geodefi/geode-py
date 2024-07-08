# -*- coding: utf-8 -*-

from src.globals import ID_TYPE

from .id import Id


class Operator(Id):
    def __init__(self, *args, **kwargs):
        """
        Initializes an Operator object.

        Parameters:
            *args: variable length argument list.
            **kwargs: arbitrary keyword arguments.
        """
        # The type of the Operator is 4
        super().__init__(*args, **kwargs, type_=ID_TYPE(4))

    @property
    def initiated(self):
        return self._read_uint("initiated")

    @property
    def maintainer(self):
        return self._read_address("maintainer")

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
    def periodSwitch(self):
        return self._read_uint("periodSwitch")

    @property
    def priorPeriod(self):
        return self._read_uint("priorPeriod")

    @property
    def validatorPeriod(self):
        return self._read_uint("validatorPeriod")

    @property
    def wallet(self):
        return self._read_uint("wallet")

    @property
    def release(self):
        return self._read_uint("release")
