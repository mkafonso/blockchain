from apps.backend.helpers.utils import hash256

class BlockHeader:
    """
    The header of a block in the blockchain.
    """

    def __init__(self, version, prev_block_hash, merkle_root, timestamp, bits):
        """
        Initialize a new block header.

        :param version: The version of the block.
        :param prev_block_hash: The hash of the previous block in the blockchain.
        :param merkle_root: The root of the Merkle tree of the transactions in the block.
        :param timestamp: The timestamp of the block.
        :param bits: The bits of the block.
        :param nonce: The nonce of the block.
        """
        self.version = version
        self.prev_block_hash = prev_block_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0
        self.block_hash = ''


    def mine(self, difficulty):
        """
        Mine the block.

        :param difficulty: The difficulty of the mining.
        """
        while self.block_hash[:difficulty] != '0' * difficulty:
            self.block_hash = hash256(self.serialize())
            self.nonce += 1


    def serialize(self):
        """
        Serialize the block header.

        :return: The serialized block header.
        """
        return f"{self.version}{self.prev_block_hash}{self.merkle_root}{self.timestamp}{self.bits}{self.nonce}"
