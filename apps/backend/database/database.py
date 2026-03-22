import json
import os


class BaseDatabase:
    """
    The base database.
    """
    def __init__(self):
        """
        Initialize the base database.
        """
        self.repo_root = "data"
        self.filename = "blockchain.json"
        self.filepath = os.path.join(self.repo_root, self.filename)


    def write(self, data):
        """
        Write data to the database.

        :param data: The data to write.
        """
        os.makedirs(self.repo_root, exist_ok=True)

        chain = []
        try:
            existing = self.read()
            if isinstance(existing, list):
                chain = existing
            elif existing is not None:
                chain = [existing]
        except (FileNotFoundError, json.JSONDecodeError):
            chain = []

        chain.append(data)
        with open(self.filepath, 'w+') as f:
            json.dump(chain, f)


    def read(self):
        """
        Read data from the database.

        :return: The data read from the database.
        """
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        return data


class Database(BaseDatabase):
    """
    The database.
    """

    def __init__(self):
        """
        Initialize the database.
        """
        super().__init__()


    def get_last_block(self):
        """
        Get the last block from the database.

        :return: The last block from the database.
        """
        try:
            data = self.read()
            if isinstance(data, list):
                return data[-1]
            if isinstance(data, dict):
                return data
            return None
        except (FileNotFoundError, json.JSONDecodeError, IndexError):
            return None
