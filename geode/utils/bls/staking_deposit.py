from typing import List
from unicodedata import normalize
from Crypto.Hash import (
    SHA256 as _sha256,
    SHA512 as _sha512,
)
from Crypto.Protocol.KDF import (
    scrypt as _scrypt,
    HKDF as _HKDF,
    PBKDF2 as _PBKDF2,
)

from py_ecc.optimized_bls12_381 import curve_order as bls_curve_order
from py_ecc.bls import G2ProofOfPossession as bls

from geode.utils.bls.serialize import (DepositMessage,
                                       compute_deposit_domain,
                                       compute_signing_root,
                                       DepositData)
from geode.globals.constants import DEPOSIT_CLI_VERSION
from geode.globals.beacon import DEPOSIT_SIZE, GENESIS_FORK_VERSION


def from_mnemonic(mnemonic: str,
                  mnemonic_password: str,
                  chain_name: str,
                  start_index: int,
                  num_keys: int,
                  hex_eth1_withdrawal_address=None):

    key_indices = range(start_index, start_index + num_keys)

    # Set path as EIP-2334 format
    # https://eips.ethereum.org/EIPS/eip-2334
    purpose = '12381'
    coin_type = '3600'

    deposit_data = []

    for amount in [DEPOSIT_SIZE.PROPOSAL, DEPOSIT_SIZE.STAKE]:
        for index in key_indices:
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

            # if hex_eth1_withdrawal_address is not None:

            withdrawal_pk = bls.SkToPk(withdrawal_sk)
            withdrawal_credentials = SHA256(withdrawal_pk)[1:]
            # else:
            #    withdrawal_credentials = ETH1_ADDRESS_WITHDRAWAL_PREFIX
            #    withdrawal_credentials += b'\x00' * 11
            #    withdrawal_credentials += hex_eth1_withdrawal_address

            deposit_message = DepositMessage(
                pubkey=bls.SkToPk(signing_sk),
                withdrawal_credentials=withdrawal_credentials,
                amount=amount,
            )

            domain = compute_deposit_domain(
                fork_version=GENESIS_FORK_VERSION[chain_name])
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
                {'fork_version': GENESIS_FORK_VERSION[chain_name]})
            datum_dict.update({'network_name': chain_name})
            datum_dict.update({'deposit_cli_version': DEPOSIT_CLI_VERSION})
            deposit_data.append(datum_dict)

    return deposit_data


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
    compliant with BIP39 mnemonics that use passwords, but is not used by this CLI outside of tests.
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


def PBKDF2(*, password: bytes, salt: bytes, dklen: int, c: int, prf: str) -> bytes:
    if 'sha' not in prf:
        raise ValueError(f"String 'sha' is not in `prf`({prf})")
    if 'sha256' in prf and c < 2**18:
        '''
        Verify the number of rounds of SHA256-PBKDF2. SHA512 not checked as use in BIP39
        does not require, and therefore doesn't use, safe parameters (c=2048).

        Ref: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki#from-mnemonic-to-seed
        '''
        raise ValueError("The PBKDF2 parameters chosen are not secure.")
    _hash = _sha256 if 'sha256' in prf else _sha512
    res = _PBKDF2(password=password, salt=salt, dkLen=dklen,
                  count=c, hmac_hash_module=_hash)  # type: ignore
    # PyCryptodome can return Tuple[bytes]
    return res if isinstance(res, bytes) else res[0]


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


def HKDF(*, salt: bytes, IKM: bytes, L: int, info: bytes = b'') -> bytes:
    res = _HKDF(master=IKM, key_len=L, salt=salt,
                hashmod=_sha256, context=info)
    # PyCryptodome can return Tuple[bytes]
    return res if isinstance(res, bytes) else res[0]


def SHA256(x: bytes) -> bytes:
    return _sha256.new(x).digest()


def _HKDF_mod_r(*, IKM: bytes, key_info: bytes = b'') -> int:
    """
    Hashes the IKM using HKDF and returns the answer as an int modulo r, the BLS field order.

    Ref: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2333.md#hkdf_mod_r
    """
    L = 48  # `ceil((3 * ceil(log2(r))) / 16)`, where `r` is the order of the BLS 12-381 curve
    salt = b'BLS-SIG-KEYGEN-SALT-'
    SK = 0
    while SK == 0:
        salt = SHA256(salt)
        okm = HKDF(
            salt=salt,
            IKM=IKM + b'\x00',  # add postfix `I2OSP(0, 1)`
            L=L,
            info=key_info + L.to_bytes(2, 'big'),
        )
        SK = int.from_bytes(okm, byteorder='big') % bls_curve_order
    return SK


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
