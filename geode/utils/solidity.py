import codecs
import hexbytes


def toBytes(key: str):
    encoded = codecs.encode(key.encode('utf-8'), 'hex_codec')
    return str('0x' + encoded.decode('utf-8'))


def toBytes32(key: str):
    if isinstance(key, hexbytes.main.HexBytes) and len(key) == 32:
        return key

    elif len(key) > 32:
        raise

    encoded = codecs.encode(key.encode('utf-8'), 'hex_codec')
    padded = encoded + b'0' * (64 - len(encoded))
    return str('0x' + padded.decode('utf-8'))


def toString(key: bytes):
    return key.decode()


def abiEncodepacked(*args) -> str:
    """
    Functions as abi.encodePacked() in Solidity
    """

    if not args:
        return ""

    encodedBytes = '0x'

    for arg in args:
        if isinstance(arg, int):
            encodedBytes += intToHexString(arg)
        else:
            raise ValueError("abiEncodepacked works only with integers")

    return encodedBytes


def intToHexString(number: int) -> str:
    """
    integer to hex string
    31 -> "(0x)000000000000000000000000000000000000001f"
    """
    hexNumber = hex(number).lstrip('0x')  # slice the 0x part

    repeatZero = int(64 - len(hexNumber))
    theEncodedData = '0'*repeatZero + hexNumber
    return theEncodedData
