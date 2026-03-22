class Block:
    """
    A block in the blockchain.
    """

    def __init__(self, height, block_size, block_header, tx_count, txs):
        """
        Initialize a new block.

        :param height: The height of the block in the blockchain.
        :param block_size: The size of the block.
        :param block_header: The header of the block.
        :param tx_count: The number of transactions in the block.
        :param txs: The transactions in the block.
        """
        self.height = height
        self.block_size = block_size
        self.block_header = block_header
        self.tx_count = tx_count
        self.txs = txs
