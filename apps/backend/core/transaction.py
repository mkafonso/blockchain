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
