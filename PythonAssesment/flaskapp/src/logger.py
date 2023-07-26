import logging
import os
from pathlib import Path


class SetupLogging:
    """Setups log file for storing application logs
    Required Params:
    - logFolderName
    - logFileName
    """
    def __init__(self, log_folder='logs', log_file='application.log'):
        self.dir = Path(__file__).parents[1]
        log_file = os.path.join(self.dir, log_folder, log_file)
        if not os.path.exists(os.path.join(self.dir, log_folder)):
            os.makedirs(os.path.join(self.dir, log_folder))
        log_handler = logging.FileHandler(log_file)
        log_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(log_handler)
