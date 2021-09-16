"""
The logging configuration of our CryptoSuite
"""
import logging
import sys
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


class Logger:
    """
    Our logging configuration
    """
    FORMATTER = logging.Formatter(
        "%(asctime)s [%(name)s][%(levelname)s] %(message)s"
    )
    TIME = str(datetime.today())[:-7]
    FORMATTED_TIME = TIME.replace("-", "_").replace(" ", "__").replace(":", "_")

    NAME = str(__file__).split('/', -1)[-1].split('.', -1)[0]

    def __init__(self):
        self.BASE_DIR = self.base_dir
        self.LOG_DIR = self.log_dir
        self.LOG_FILE = self.log_file

    @property
    def base_dir(self):
        self.BASE_DIR = os.path.abspath(os.getcwd())
        self.BASE_DIR.split("CryptoSuite", 1)[1] = "CryptoSuite"
        return self.BASE_DIR

    @property
    def log_dir(self):
        self.LOG_DIR = "/".join([self.BASE_DIR, "log"])
        return self.LOG_DIR

    @property
    def log_file(self):
        self.LOG_FILE = "/".join([
            self.LOG_DIR,
            f"{self.NAME}_{self.FORMATTED_TIME}.log"
        ])
        return self.LOG_FILE

    def get_console_handler(self):
        """
        setting up the handler for logging sent to the console
        :return: console_handler
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.FORMATTER)
        return console_handler

    def get_file_handler(self):
        """
        setting up the handler for logging sent to a logfile
        log location: ./log/{app_name}_{FORMATTED_TIME}.log
        :return: file_handler
        """
        file_handler = TimedRotatingFileHandler(self.LOG_FILE, when='midnight')
        file_handler.setFormatter(self.FORMATTER)
        return file_handler

    def setup_logger(self):
        """

        :param name: name of your logger
        :return: logger
        """
        log = logging.getLogger(self.NAME)
        log.setLevel(logging.DEBUG)
        log.addHandler(self.get_console_handler())
        log.addHandler(self.get_file_handler())
        log.propagate = False
        return log


# logger = Logger().setup_logger()
