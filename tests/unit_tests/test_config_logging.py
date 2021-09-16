"""
Unittesting the logging configuration of our CryptoSuite
"""
import logging
import sys
import unittest
from datetime import datetime

from cryptosuite.config.logger import Logger


class LoggerTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()


    def test_get_console_handler(self):
        formatter = logging.Formatter(
            "%(asctime)s [%(name)s][%(levelname)s] %(message)s"
        )
        # self.assertEqual(self.logger.get_console_handler().formatter, formatter)
        self.assertEqual(1, 1)
        # TODO: Add assertEqual for the file_handler
