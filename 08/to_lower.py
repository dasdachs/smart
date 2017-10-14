#! /usr/bin/env python2
# -*- coding: utf-8 -*- 
"""Return the input text in lower case."""
import argparse

parser = argparse.ArgumentParser(description='Transforms text to lower case.')
parser.add_argument('text', type=str, nargs="+", help='Text that will be transformed to lower case.')
args = parser.parse_args()

if __name__ == "__main__":
    print " ".join(args.text).lower()

