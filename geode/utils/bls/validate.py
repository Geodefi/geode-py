from eth_typing import (
    BLSPubkey,
    BLSSignature,
)
from typing import Any, Dict, List
from py_ecc.bls import G2ProofOfPossession as bls
from Crypto.Hash import SHA256 as _sha256

from geode.globals import (
    MIN_DEPOSIT_AMOUNT,
    MAX_DEPOSIT_AMOUNT)

from .serialize import (DepositMessage,
                        compute_deposit_domain,
                        compute_signing_root,
                        DepositData)

from .staking_deposit import from_mnemonic


def SHA256(x: bytes) -> bytes:
    return _sha256.new(x).digest()


def validate_deposit(deposit_data_dict: Dict[str, Any]) -> bool:
    '''
    Checks whether a deposit is valid based on the staking deposit rules.
    https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/beacon-chain.md#deposits
    '''
    pubkey = BLSPubkey(bytes.fromhex(deposit_data_dict['pubkey']))
    withdrawal_credentials = bytes.fromhex(
        deposit_data_dict['withdrawal_credentials'])
    amount = deposit_data_dict['amount']
    signature = BLSSignature(bytes.fromhex(deposit_data_dict['signature']))
    deposit_message_root = bytes.fromhex(
        deposit_data_dict['deposit_data_root'])
    fork_version = bytes.fromhex(deposit_data_dict['fork_version'])

    # Verify pubkey
    if len(pubkey) != 48:
        return False

    # Verify deposit signature && pubkey
    deposit_message = DepositMessage(
        pubkey=pubkey, withdrawal_credentials=withdrawal_credentials, amount=amount)
    domain = compute_deposit_domain(fork_version)
    signing_root = compute_signing_root(deposit_message, domain)
    if not bls.Verify(pubkey, signing_root, signature):
        return False

    # Verify Deposit Root
    signed_deposit = DepositData(
        pubkey=pubkey,
        withdrawal_credentials=withdrawal_credentials,
        amount=amount,
        signature=signature,
    )
    return signed_deposit.hash_tree_root == deposit_message_root


def validate_parameters(pubkey, withdrawal_credentials, amount, signature, fork_version) -> bool:
    """
    :param: pubkey (str) ==> len-96 "No 0x-prefix" public key.
    :param: withdrawal_credentials (str) ==>  len-96 "No 0x-prefix"
    :param: amount (int) ==> 31000000000 for 31 and 1000000000 for 1.
    :param: signature (str) ==>  len-192 "No 0x-prefix" 
    :param: fork_version (bytes) ==>  fork_version

    return True if the parameters can be validated, else otherwise.
    """

    # pubkey
    pubkey = BLSPubkey(bytes.fromhex(pubkey))

    # withdrawal_credentials
    withdrawal_credentials = bytes.fromhex(withdrawal_credentials)

    # signature
    signature = bytes.fromhex(signature)

    # Form deposit masage
    deposit_message = DepositMessage(
        pubkey=pubkey, withdrawal_credentials=withdrawal_credentials, amount=amount)

    domain = compute_deposit_domain(fork_version)
    signing_root = compute_signing_root(deposit_message, domain)

    return bls.Verify(pubkey, signing_root, signature)

# createDepositData(index, mnemonic_key varsa al yoksa yeniden yarat, lenght) => json


def createDepositData(start_index: int, mnemonics: str, mnemonic_password: str, num_keys: int) -> List[Dict]:
    return from_mnemonic(mnemonics, mnemonic_password, 'goerli', start_index, num_keys)


"""
sample = [{
    "pubkey": "a63bd7ac6ec058a2ceb2dcae56798d52111d8a38bef90574bf08bb09144c678f1eb02fd801ec610bf2b23820b4742814",
    "withdrawal_credentials": "002dddf0cb7bea8104d37b1b830caf7032b8842ed71ffb9a1649e821c15934f9",
    "amount": 31000000000,
    "signature": "8ad9a61b74bcce247f1ccf5215ab250cd90320febf05ab73f9a00b31cc0d8c898cb99b71e3c68faf6112f6341ae1fecf0a4ab26cd66d21c90f9f078a65584dc547cd024a86089d028a407f9f4673d34875f67af115714fda163143acc9ba21b7",
    "deposit_message_root": "d25d4047d37cbe5e7a7061421ea30abd7fcbc3547842b8e48b215a0d5c641550",
    "deposit_data_root": "d922440f1ffe241e1af054e2a3660ba2a810ff48f5701721534a3c307cfb916e",
    "fork_version": "00001020",
    "network_name": "goerli",
    "deposit_cli_version": "2.3.0"}]
"""
