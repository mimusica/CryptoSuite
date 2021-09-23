#!/usr/bin/env python3
"""
Welcome to the CryptoSuite!

In our Suite you'll find a nice ensemble of tools that assist with the
interaction of various segments of the Crypto universe.
"""
from argparse import ArgumentParser

from cryptosuite import __version__

parser = ArgumentParser()
parser.add_argument('-v', '--version',
                    help="Version info",
                    action='store_true'
                    )
args = parser.parse_args()

if args.version:
    print(__version__)
