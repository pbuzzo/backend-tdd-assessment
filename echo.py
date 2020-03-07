#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

import sys
import argparse


__author__ = "Patrick Buzzo"
""" Helping Hand From: Piero and Kano """


def create_parser():
    """Creates a parser for dotm searcher"""
    parser = argparse.ArgumentParser(
        description='Searches for text within all dotm files in a directory')
    parser.add_argument(
        '-u', help='directory to search for dotm files')
    parser.add_argument(
        '-l', help='directory to search for dotm files')
    parser.add_argument("-h", "--help", help='Help: Information on Usage')
    parser.add_argument(
        "-u", "--upper", help='Find The Upper-Cased Version Of Input')
    parser.add_argument(
        "-l", "--lower", help='Find The Lower-Cased Version Of Input')
    parser.add_argument(
        "-t", "--title", help='Find The Capitalized (Title) Version Of Input')
    parser.add_argument('-t', help='text to search within each dotm file')
    return parser


def main(args):
    # parser = create_parser()
    # namespace = parser.parse_args(args)

    # return transformed_text
    pass
    # parser = create_parser()
    # # Run the parser to collect command-line arguments
    # # into a NAMESPACE called 'ns'
    # ns = parser.parse_args(args)

    # if not ns:
    #     parser.print_usage()
    #     sys.exit(1)

    # file_list = ns.files

    # # option flag
    # create_summary = ns.summaryfile

    # if create_summary:
    #     if file_list[0] == 'hello':


if __name__ == "__main__":
    print(main(sys.argv[1:]))
