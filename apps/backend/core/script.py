class Script:
    """
    A script in the blockchain.
    """

    def __init__(self, scripts = None):
        """
        Initialize a script.

        :param scripts: The scripts.
        """

        if scripts is None:
            self.scripts = []
        else:
            self.scripts = scripts
