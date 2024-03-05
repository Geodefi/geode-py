import codecs
import hexbytes


def to_bytes(key: str):
    encoded = codecs.encode(key.encode("utf-8"), "hex_codec")
    return str("0x" + encoded.decode("utf-8"))


def to_bytes32(key: str):
    if isinstance(key, hexbytes.main.HexBytes) and len(key) == 32:
        return key

    encoded = codecs.encode(key.encode("utf-8"), "hex_codec")
    padded = encoded + b"0" * (64 - len(encoded))
    return str("0x" + padded.decode("utf-8"))


def to_string(key: bytes):
    return key.decode()
