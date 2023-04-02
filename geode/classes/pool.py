import typing as t

from geode.globals import ID_TYPE, DEPOSIT_SIZE
from geode.utils import getKey, validate_deposit_data_file


from .id import Id
from .validator import Validator
from .beacon import Beacon


class Pool(Id):

    def __init__(self, beacon: Beacon, *args, **kwargs):
        self.TYPE: ID_TYPE(5)
        self.Beacon: Beacon = beacon
        super().__init__(*args, **kwargs)

    @property
    def initiated(self):
        return self._readUint("initiated")

    @property
    def maintainer(self):
        return self._readAddress("maintainer")

    @property
    def surplus(self):
        return self._readUint("surplus")

    @property
    def secured(self):
        return self._readUint("secured")

    def allowance(self, operator: int):
        return self._readUint(getKey(id=operator, key="allowance"))

    def proposedValidators(self, operator: int):
        return self._readUint(getKey(id=operator, key="proposedValidators"))

    def activeValidators(self, operator: int):
        return self._readUint(getKey(id=operator, key="activeValidators"))

    @property
    def interfacesList(self):
        lenInterfaces = self.interfacesLen
        ints: t.List = []
        for i in range(lenInterfaces):
            ints.append(self._readAddressArray("interfaces", i))
        return ints

    @property
    def interfacesLen(self):
        return self._readUint("interfaces")

    def interfaces(self, index):
        return self._readAddressArray("interfaces", index)

    @property
    def private(self):
        return (self._readUint("private") == 1)

    @property
    def whitelist(self):
        return self._readAddress("whitelist")

    @property
    def withdrawalCredential(self):
        return self._readBytes("withdrawalCredential", isHex=True)

    @property
    def withdrawalContract(self):
        return self._readAddress("withdrawalContract")

    @property
    def liquidityPool(self):
        return self._readAddress("liquidityPool")

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
    def wallet(self):
        return self._readUint("wallet")

    @property
    def validatorsList(self):
        lenvalidators = self.validatorsLen
        vals: t.List = []
        for i in range(lenvalidators):
            vals.append(self._readBytesArray(
                "validators", index=i))
        return vals

    @property
    def validatorsLen(self):
        return self._readUint("validators")

    def validators(self, index):
        return Validator(network=self.network, beacon=self.Beacon, w3=self.w3, portal=self.portal,
                         pk=self._readBytesArray("validators", index=index))

    def prepareProposeStake(self, deposit_data_path: str):
        deposit_data = validate_deposit_data_file(deposit_data_path=deposit_data_path,
                                                  amount=DEPOSIT_SIZE.PROPOSAL,
                                                  network=self.network,
                                                  credential=self.withdrawalCredential[2:])
        pubkeys = [bytes.fromhex(deposit['pubkey'])
                   for deposit in deposit_data]
        sig1s = [bytes.fromhex(deposit['signature'])
                 for deposit in deposit_data]
        return pubkeys, sig1s

    def prepareBeaconStake(self, deposit_data_path: str):
        deposit_data = validate_deposit_data_file(deposit_data_path=deposit_data_path,
                                                  amount=DEPOSIT_SIZE.BEACON,
                                                  network=self.network,
                                                  credential=self.withdrawalCredential[2:])
        pubkeys = [bytes.fromhex(deposit['pubkey'])
                   for deposit in deposit_data]
        sig31s = [bytes.fromhex(deposit['signature'])
                  for deposit in deposit_data]
        return pubkeys, sig31s
