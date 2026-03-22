import hashlib
from Crypto.Hash import RIPEMD160
from hashlib import sha256
from math import log

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


def int_to_little_endian(n, length):
    """
    Convert an integer to a little-endian byte string.

    :param n: The integer to convert.
    :param length: The length of the byte string.
    :return: The little-endian byte string.
    """
    return n.to_bytes(length, byteorder="little")


def bytes_needed_for_little_endian(n):
    """
    Calculate the number of bytes needed to represent an integer in little-endian format.

    :param n: The integer to convert.
    :return: The number of bytes needed.
    """
    if n == 0:
        return 1
    return int(log(n, 256)) + 1
