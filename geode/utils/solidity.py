import codecs
import hexbytes


def toBytes(key: str):
    encoded = codecs.encode(key.encode('utf-8'), 'hex_codec')
    return str('0x' + encoded.decode('utf-8'))


def toBytes32(key: str):
    if isinstance(key, hexbytes.main.HexBytes) and len(key) == 32:
        return key

    encoded = codecs.encode(key.encode('utf-8'), 'hex_codec')
    padded = encoded + b'0' * (64 - len(encoded))
    return str('0x' + padded.decode('utf-8'))


def toString(key: bytes):
    return key.decode()
