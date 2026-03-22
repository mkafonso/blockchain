from apps.backend.helpers.utils import int_to_little_endian, bytes_needed_for_little_endian


REWARD = 50
SIGHASH_ALL = 1
ZERO_HASH = b"\0" * 32
MINER_ADDRESS = "1LYgXwYXw16GJXgDwHV7aCNijnQWYEdc1C"
PRIVATE_KEY = (
    "59024195091230105596801455306913435815673319996141880726735464739248197324364"
)


class Transaction:
    """
    A transaction in the blockchain.
    """

    def __init__(self, version, tx_ins, tx_outs, lock_time):
        """
        Initialize a transaction.

        :param version: The version of the transaction.
        :param tx_ins: The transaction inputs.
        :param tx_outs: The transaction outputs.
        :param lock_time: The lock time of the transaction.
        """
        self.version = version
        self.tx_ins = tx_ins
        self.tx_outs = tx_outs
        self.lock_time = lock_time


class TransactionInput:
    """
    A transaction input in the blockchain.
    """

    def __init__(self, prev_tx, prev_index, script_sig=None, sequence=0xFFFFFFFF):
        """
        Initialize a transaction input.

        :param prev_tx: The previous transaction.
        :param prev_index: The index of the previous transaction output.
        :param script_sig: The script signature.
        :param sequence: The sequence number.
        """
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        self.sequence = sequence
        if script_sig is None:
            self.script_sig = Script()
        else:
            self.script_sig = script_sig


class TransactionOutput:
    """
    A transaction output in the blockchain.
    """

    def __init__(self, value, script_pub_key=None):
        """
        Initialize a transaction output.

        :param value: The value of the transaction output.
        :param script_pub_key: The script public key.
        """
        self.value = value
        if script_pub_key is None:
            self.script_pub_key = Script()
        else:
            self.script_pub_key = script_pub_key


class Coinbase(Transaction):
    """
    A coinbase transaction in the blockchain.
    """

    def __init__(self, block_height):
        """
        Initialize a coinbase transaction.

        :param block_height: The block height.
        """
        self.block_height_in_little_endian = int_to_little_endian(block_height, bytes_needed_for_little_endian(block_height))


    def CoinbaseTransaction(self):
        """
        Create a coinbase transaction.

        :return: The coinbase transaction.
        """
        prev_tx = ZERO_HASH
        prev_index = 0xFFFFFFFF
        tx_ins = []
        tx_ins.append(TxIn(prev_tx, prev_index))
        tx_ins[0].script_sig.cmds.append(self.BlockHeightInLittleEndian)

        tx_outs = []
        target_amount = REWARD * 100000000
        target_h160 = decode_base58(MINER_ADDRESS)
        target_script = Script.p2pkh_script(target_h160)
        tx_outs.append(TxOut(amount=target_amount, script_pubkey=target_script))
        coinBaseTx = Tx(1, tx_ins, tx_outs, 0)
        coinBaseTx.TxId = coinBaseTx.id()

        return coinBaseTx
