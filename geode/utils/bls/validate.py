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

from .ssz import (DepositMessage,
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
    # if pubkey != credential.signing_pk:
    #     return False

    # # Verify withdrawal credential
    # if len(withdrawal_credentials) != 32:
    #     return False
    # if withdrawal_credentials[:1] == BLS_WITHDRAWAL_PREFIX == credential.withdrawal_prefix:
    #     if withdrawal_credentials[1:] != SHA256(credential.withdrawal_pk)[1:]:
    #         return False
    # elif withdrawal_credentials[:1] == ETH1_ADDRESS_WITHDRAWAL_PREFIX == credential.withdrawal_prefix:
    #     if withdrawal_credentials[1:12] != b'\x00' * 11:
    #         return False
    #     if credential.eth1_withdrawal_address is None:
    #         return False
    #     if withdrawal_credentials[12:] != credential.eth1_withdrawal_address:
    #         return False
    # else:
    #     return False

    # Verify deposit amount
    # if not MIN_DEPOSIT_AMOUNT < amount <= MAX_DEPOSIT_AMOUNT:
    #     return False

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
