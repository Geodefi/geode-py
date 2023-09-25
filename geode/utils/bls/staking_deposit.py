from typing import List, Optional
from unicodedata import normalize
from dataclasses import asdict

from py_ecc.optimized_bls12_381 import curve_order as bls_curve_order
from py_ecc.bls import G2ProofOfPossession as bls

from geode.utils.bls.serialize import (DepositMessage,
                                       compute_deposit_domain,
                                       compute_signing_root,
                                       DepositData)

from geode.utils.bls.keystore import (ScryptKeystore,
                                      Keystore)

from geode.utils.bls.crypto import (SHA256,
                                    HKDF,
                                    _HKDF_mod_r,
                                    PBKDF2
                                    )

from geode.globals.constants import DEPOSIT_CLI_VERSION, WORD_LIST_PATH, ETH1_ADDRESS_WITHDRAWAL_PREFIX
from geode.globals.beacon import DEPOSIT_SIZE, GENESIS_FORK_VERSION, DEPOSIT_NETWORK_NAME


import os
from random import SystemRandom

_sysrand = SystemRandom()

randbits = _sysrand.getrandbits


def from_mnemonic(mnemonic: str,
                  mnemonic_password: str,
                  chain_id: int,
                  start_index: int,
                  num_keys: int,
                  hex_eth1_withdrawal_address):

    key_indices = range(start_index, start_index + num_keys)

    # Set path as EIP-2334 format
    # https://eips.ethereum.org/EIPS/eip-2334
    purpose = '12381'
    coin_type = '3600'

    deposit_data = []
    keystore_data = []

    for index in key_indices:
        for_each_pubkey = []
        for amount in [DEPOSIT_SIZE.PROPOSAL.value, DEPOSIT_SIZE.STAKE.value]:
            account = str(index)
            withdrawal_key_path = f'm/{purpose}/{coin_type}/{account}/0'
            signing_key_path = f'{withdrawal_key_path}/0'

            withdrawal_sk = mnemonic_and_path_to_key(
                mnemonic=mnemonic, path=withdrawal_key_path, password=mnemonic_password)
            signing_sk = mnemonic_and_path_to_key(
                mnemonic=mnemonic, path=signing_key_path, password=mnemonic_password)
            """
            Return a single deposit datum for 1 validator including all
            the information needed to verify and process the deposit.
            """

            withdrawal_pk = bls.SkToPk(withdrawal_sk)
            withdrawal_credentials = SHA256(withdrawal_pk)[1:]

            if hex_eth1_withdrawal_address is None:
                raise Exception("#TODO")

            else:
                withdrawal_credentials = ETH1_ADDRESS_WITHDRAWAL_PREFIX
                withdrawal_credentials += b'\x00' * 11
                withdrawal_credentials += hex_eth1_withdrawal_address

            deposit_message = DepositMessage(
                pubkey=bls.SkToPk(signing_sk),
                withdrawal_credentials=withdrawal_credentials,
                amount=amount,
            )

            domain = compute_deposit_domain(
                fork_version=GENESIS_FORK_VERSION[chain_id])
            signing_root = compute_signing_root(deposit_message, domain)
            signed_deposit = DepositData(
                **deposit_message.as_dict(),
                signature=bls.Sign(signing_sk, signing_root)
            )

            signed_deposit_datum = signed_deposit
            datum_dict = signed_deposit_datum.as_dict()
            datum_dict.update(
                {'deposit_message_root': deposit_message.hash_tree_root})
            datum_dict.update(
                {'deposit_data_root': signed_deposit_datum.hash_tree_root})
            datum_dict.update(
                {'fork_version': GENESIS_FORK_VERSION[chain_id]})
            datum_dict.update({'network_name': DEPOSIT_NETWORK_NAME[chain_id]})
            datum_dict.update({'deposit_cli_version': DEPOSIT_CLI_VERSION})

            for_each_pubkey.append(datum_dict)

        keystore_data.append(signing_keystore(
            signing_sk, signing_key_path, mnemonic_password))
        deposit_data.append(for_each_pubkey)

    return deposit_data, keystore_data


def get_mnemonic(*, entropy: Optional[bytes] = None) -> str:
    """
    Return a mnemonic string in a given `language` based on `entropy` via the calculated checksum.

    Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#generating-the-mnemonic
    """
    if entropy is None:
        entropy = randbits(256).to_bytes(32, 'big')
    entropy_length = len(entropy) * 8
    checksum_length = (entropy_length // 32)
    checksum = _get_checksum(entropy)
    entropy_bits = int.from_bytes(entropy, 'big') << checksum_length
    entropy_bits += checksum
    entropy_length += checksum_length
    mnemonic = []
    word_list = _get_word_list(WORD_LIST_PATH)
    for i in range(entropy_length // 11 - 1, -1, -1):
        index = (entropy_bits >> i * 11) & 2**11 - 1
        word = _index_to_word(word_list, index)
        mnemonic.append(word)
    return ' '.join(mnemonic)


def _get_checksum(entropy: bytes) -> int:
    """
    Determine the index of the checksum word given the entropy
    """
    _validate_entropy_length(entropy)
    checksum_length = len(entropy) // 4
    return int.from_bytes(SHA256(entropy), 'big') >> (256 - checksum_length)


def _get_word_list(path: str) -> List[str]:
    """
    Given the language and path to the wordlist, return the list of BIP39 words.

    Ref: https://github.com/bitcoin/bips/blob/master/bip-0039/bip-0039-wordlists.md
    """
    dirty_list = open(os.path.join(path, 'word_list.txt'),
                      encoding='utf-8').readlines()
    return [word.replace('\n', '') for word in dirty_list]


def _index_to_word(word_list: List[str], index: int) -> str:
    """
    Return the corresponding word for the supplied index while stripping out '\\n' chars.
    """
    if index >= 2048:
        raise IndexError(f"`index` should be less than 2048. Got {index}.")
    return word_list[index]


def _validate_entropy_length(entropy: bytes) -> None:
    entropy_length = len(entropy) * 8
    if entropy_length not in range(128, 257, 32):
        raise IndexError(
            f"`entropy_length` should be in [128, 160, 192, 224, 256]. Got {entropy_length}.")


def path_to_nodes(path: str) -> List[int]:
    """
    Maps from a path string to a list of indices where each index represents the corresponding level in the path.
    """
    path = path.replace(' ', '')
    if not set(path).issubset(set('m1234567890/')):
        raise ValueError(f"Invalid path {path}")

    indices = path.split('/')

    if indices[0] != 'm':
        raise ValueError(
            f"The first character of path should be `m`. Got {indices[0]}.")
    indices.pop(0)

    return [int(index) for index in indices]


def mnemonic_and_path_to_key(*, mnemonic: str, path: str, password: str) -> int:
    """
    Return the SK at position `path`, derived from `mnemonic`. The password is to be
    compliant with BIP39 mnemonic that use passwords, but is not used by this CLI outside of tests.
    """
    seed = get_seed(mnemonic=mnemonic, password=password)
    sk = derive_master_SK(seed)
    for node in path_to_nodes(path):
        sk = derive_child_SK(parent_SK=sk, index=node)
    return sk


def get_seed(*, mnemonic: str, password: str) -> bytes:
    """
    Derive the seed for the pre-image root of the tree.

    Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#from-mnemonic-to-seed
    """
    encoded_mnemonic = normalize('NFKD', mnemonic).encode('utf-8')
    salt = normalize('NFKD', 'mnemonic' + password).encode('utf-8')
    return PBKDF2(password=encoded_mnemonic, salt=salt, dklen=64, c=2048, prf='sha512')


def derive_child_SK(*, parent_SK: int, index: int) -> int:
    """
    Given a parent SK `parent_SK`, return the child SK at the supplied `index`.

    Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2333.md#derive_child_sk
    """
    if index < 0 or index >= 2**32:
        raise IndexError(
            f"`index` should be greater than or equal to  0 and less than 2**32. Got index={index}.")
    lamport_PK = _parent_SK_to_lamport_PK(parent_SK=parent_SK, index=index)
    return _HKDF_mod_r(IKM=lamport_PK)


def derive_master_SK(seed: bytes) -> int:
    """
    Given a seed, derive the master SK.

    Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2333.md#derive_master_sk
    """
    if len(seed) < 32:
        raise ValueError(
            f"`len(seed)` should be greater than or equal to 32. Got {len(seed)}.")
    return _HKDF_mod_r(IKM=seed)


def _flip_bits_256(input: int) -> int:
    """
    Flips 256 bits worth of `input`.
    """
    return input ^ (2**256 - 1)


def _IKM_to_lamport_SK(*, IKM: bytes, salt: bytes) -> List[bytes]:
    """
    Derives the lamport SK for a given `IKM` and `salt`.

    Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2333.md#ikm_to_lamport_sk
    """
    OKM = HKDF(salt=salt, IKM=IKM, L=8160)
    lamport_SK = [OKM[i: i + 32] for i in range(0, 8160, 32)]
    return lamport_SK


def _parent_SK_to_lamport_PK(*, parent_SK: int, index: int) -> bytes:
    """
    Derives the `index`th child's lamport PK from the `parent_SK`.

    Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2333.md#parent_sk_to_lamport_pk
    """
    salt = index.to_bytes(4, byteorder='big')
    IKM = parent_SK.to_bytes(32, byteorder='big')
    lamport_0 = _IKM_to_lamport_SK(IKM=IKM, salt=salt)
    not_IKM = _flip_bits_256(parent_SK).to_bytes(32, byteorder='big')
    lamport_1 = _IKM_to_lamport_SK(IKM=not_IKM, salt=salt)
    lamport_SKs = lamport_0 + lamport_1
    lamport_PKs = [SHA256(sk) for sk in lamport_SKs]
    compressed_PK = SHA256(b''.join(lamport_PKs))
    return compressed_PK


def signing_keystore(signing_sk: int, signing_key_path: str, password: str) -> Keystore:
    secret = signing_sk.to_bytes(32, 'big')
    return asdict(ScryptKeystore.encrypt(secret=secret, password=password, path=signing_key_path))
