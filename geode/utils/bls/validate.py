from eth_typing import (
    BLSPubkey,
    BLSSignature,
)
from typing import Any, Dict
from py_ecc.bls import G2ProofOfPossession as bls
from Crypto.Hash import SHA256 as _sha256

from geode.globals import (
    MIN_DEPOSIT_AMOUNT,
    MAX_DEPOSIT_AMOUNT)

from .serialize import (DepositMessage,
                        compute_deposit_domain,
                        compute_signing_root,
                        DepositData)


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
