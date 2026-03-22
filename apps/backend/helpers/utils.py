import hashlib

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
