import typing as t

from geodefi.globals import ID_TYPE, DEPOSIT_SIZE
from geodefi.utils import get_key, validate_deposit_data_file


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

    def prepareProposeStake(self, deposit_data_path: str):
        """
        This method prepares for a validator proposal. It reads deposit data from a file path,
        validates it, and returns the public keys and signature 1s for the proposal stake.

        Args:
        - deposit_data_path (str): The file path of the deposit data.

        Returns:
        - pubkeys (List[bytes]): A list of public keys as bytes objects.
        - sig1s (List[bytes]): A list of signature 1s as bytes objects.
        """
        deposit_data = validate_deposit_data_file(
            deposit_data_path=deposit_data_path,
            amount=DEPOSIT_SIZE.PROPOSAL,
            network=self.network,
            credential=self.withdrawalCredential[2:],
        )
        pubkeys = [bytes.fromhex(deposit["pubkey"]) for deposit in deposit_data]
        sig1s = [
            bytes.fromhex(deposit["signature"]) for deposit in deposit_data
        ]
        return pubkeys, sig1s

    def prepareStake(self, deposit_data_path: str):
        """
        This function prepares a beacon stake by taking the path to a deposit data file as input.
        The deposit data file is validated by checking that it contains the required amount of Ether
        for the Beacon chain, that it is meant for the specified network, and that it is associated
        with the withdrawal credentials of the current operator.

        Once the deposit data has been validated, the function extracts the public keys and
        signatures from the deposit data and returns them as a tuple.

        Args:
            deposit_data_path (str): The path to the deposit data file.

        Returns:
            Tuple of lists: A tuple containing two lists, the public keys and signatures extracted
            from the deposit data file.
        """

        deposit_data = validate_deposit_data_file(
            deposit_data_path=deposit_data_path,
            amount=DEPOSIT_SIZE.STAKE,
            network=self.network,
            credential=self.withdrawalCredential[2:],
        )
        pubkeys = [bytes.fromhex(deposit["pubkey"]) for deposit in deposit_data]
        sig31s = [
            bytes.fromhex(deposit["signature"]) for deposit in deposit_data
        ]
        return pubkeys, sig31s
