"""
Welcome to the CryptoSuite!

In our Suite you'll find a nice ensemble of tools that assist with the
interaction of various segments of the Crypto universe.
"""
from argparse import ArgumentParser

__version__ = "0.1.0"
__author__ = "Christophe@Langenberg.be"


def __contributors__():
    with open('./CONTRIBUTORS.txt') as c:
        contributors = c.readlines()
        return contributors


def run():
    parser = ArgumentParser()
    parser.add_argument('-v', '--version',
                        help="Version info",
                        action='store_true'
                        )
    args = parser.parse_args()

    if args.version:
        print(__version__)
