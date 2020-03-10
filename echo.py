#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

import sys
import argparse


__author__ = "Patrick Buzzo"
""" Helping Hand From: Piero, Derek, and Kano """


def create_parser(*args):
    """Creates a parser for command arguments"""
    parser = argparse.ArgumentParser(
        description='Searches for text within all dotm files in a directory')
    parser.add_argument(
        '-u', "--upper", action="store_true", help='return upper-cased version')
    parser.add_argument(
        '-l', "--lower", action="store_true", help='return lower-cased version')
    parser.add_argument(
        '-t', "--title", action="store_true", help='return title-cased version')
    parser.add_argument('target', help="String to Change")
    return parser


def main(items):
    parser = create_parser()
    args = parser.parse_args(items)
    changed_str = args.target
    # check lower-cased
    if args.lower:
        changed_str = changed_str.lower()
    # check upper-cased
    if args.upper:
        changed_str = changed_str.upper()
    # check title-cased
    if args.title:
        changed_str = changed_str.title()
    return changed_str


if __name__ == "__main__":
    print(main(sys.argv[1:]))
