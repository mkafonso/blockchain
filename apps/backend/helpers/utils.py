import hashlib

def hash256(data):
    """
    Hash the data using SHA256.

    :param data: The data to hash.
    :return: The hash of the data.
    """
    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()
