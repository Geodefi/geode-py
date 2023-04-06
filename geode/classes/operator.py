from geode.globals import ID_TYPE

from .id import Id


class Operator(Id):

    def __init__(self, *args, **kwargs):
        """
        Initializes an Operator object.

        Parameters:
        *args: variable length argument list.
        **kwargs: arbitrary keyword arguments.

        Returns:
        None
        """
        self.TYPE = ID_TYPE(4)  # The type of the Operator is 4.
        super().__init__(*args, **kwargs)

    @property
    def initiated(self):
        return self._readUint("initiated")

    @property
    def maintainer(self):
        return self._readAddress("maintainer")

    @property
    def totalProposedValidators(self):
        return self._readUint("totalProposedValidators")

    @property
    def totalActiveValidators(self):
        return self._readUint("totalActiveValidators")

    @property
    def feeSwitch(self):
        return self._readUint("feeSwitch")

    @property
    def priorFee(self):
        return self._readUint("priorFee")

    @property
    def fee(self):
        return self._readUint("fee")

    @property
    def periodSwitch(self):
        return self._readUint("periodSwitch")

    @property
    def priorPeriod(self):
        return self._readUint("priorPeriod")

    @property
    def validatorPeriod(self):
        return self._readUint("validatorPeriod")

    @property
    def wallet(self):
        return self._readUint("wallet")

    @property
    def released(self):
        return self._readUint("released")
