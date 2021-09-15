"""
The logging configuration of our CryptoSuite
"""
import logging
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


FORMATTER = logging.Formatter(
    "%(asctime)s [%(name)s][%(levelname)s] %(message)s"
)
TIME = str(datetime.today())[:-7]
FORMATTED_TIME = TIME.replace("-", "_").replace(" ", "__").replace(":", "_")

LOG_DIR = "./log"
LOG_FILE = f"{LOG_DIR}/{str(__file__).split('.', 1)[0]}_{FORMATTED_TIME}.log"


def get_console_handler():
    """
    setting up the handler for logging sent to the console
    :return: console_handler
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    """
    setting up the handler for logging sent to a logfile
    log location: ./log/{app_name}_{FORMATTED_TIME}.log
    :return: file_handler
    """
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def setup_logger(logger_name):
    """

    :param logger_name: name of your logger
    :return: logger
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger


logger = setup_logger("CryptoSuite")
