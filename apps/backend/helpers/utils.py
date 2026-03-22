import hashlib
from Crypto.Hash import RIPEMD160
from hashlib import sha256

def hash256(data):
    """
    Hash the data using SHA256.

    :param data: The data to hash.
    :return: The hash of the data.
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    elif isinstance(data, (bytearray, memoryview)):
        data = bytes(data)
    elif not isinstance(data, (bytes,)):
        data = str(data).encode("utf-8")

    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()


def hash160(data):
    """
    Hash the data using HASH160 (RIPEMD160(SHA256(data))).

    :param data: Bytes to hash.
    :return: The hash digest bytes.
    """
    return RIPEMD160.new(sha256(data).digest()).digest()
