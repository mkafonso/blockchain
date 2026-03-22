import time
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(repo_root))

from apps.backend.core.block import Block
from apps.backend.core.block_header import BlockHeader
from apps.backend.helpers.utils import hash256

ZERO_HASH = '0' * 64
VERSION = 1

class Blockchain:
    """
    The blockchain.
    """

    def __init__(self):
        """
        Initialize the blockchain.
        """
        self.difficulty = 4
        self.chain = []
        self.create_genesis_block()


    def create_genesis_block(self):
        """
        Create the genesis block.
        """
        block_height = 0
        prev_block_hash = ZERO_HASH
        self.add_block(block_height, prev_block_hash)


    def add_block(self, block_height, prev_block_hash):
        """
        Add a block to the blockchain.

        :param block_height: The height of the block.
        :param prev_block_hash: The hash of the previous block.
        """
        timestamp = int(time.time())
        transaction = f"Alert sent {block_height} bitcoins to Jane Doe"
        merkle_root = hash256(transaction)
        bits = 'ffff001f'
        block_header = BlockHeader(VERSION, prev_block_hash, merkle_root, timestamp, bits)
        block_header.mine(self.difficulty)
        block_size = 1
        tx_count = 1
        block = Block(block_height, block_size, block_header, tx_count, transaction)
        self.chain.append(block)


if __name__ == '__main__':
    blockchain = Blockchain()
    print(blockchain.chain[0].__dict__)
