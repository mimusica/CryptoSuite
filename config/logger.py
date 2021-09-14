import logging
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


FORMATTER = logging.Formatter("%(asctime)s [%(name)s][%(levelname)s] %(message)s")
time = str(datetime.today())[:-7]
formatted_time = time.replace("-", "_").replace(" ", "__").replace(":", "_")

# TODO: add the correct directory -->   /log
LOG_FILE = f"{str(__file__).split('.')[0]}_{formatted_time}.log"


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger


logger = get_logger("CryptoSuite")