"""
Unittesting the logging configuration of our CryptoSuite
"""
import logging
import sys
import unittest
from datetime import datetime

import config.logger as logger


class LoggerTestCase(unittest.TestCase):
    FORMATTER = logging.Formatter(
        "%(asctime)s [%(name)s][%(levelname)s] %(message)s"
    )
    TIME = str(datetime.today())[:-7]
    FORMATTED_TIME = TIME.replace("-", "_").replace(" ", "__").replace(":", "_")

    LOG_DIR = "./log"
    LOG_FILE = f"{LOG_DIR}/{str(__file__).split('.', 1)[0]}_{FORMATTED_TIME}.log"

    def test_get_console_handler(self):
        test_console_handler = logging.StreamHandler(sys.stdout)
        test_console_handler.setFormatter(self.FORMATTER)
        self.assertEqual(logger.get_console_handler(), test_console_handler)
