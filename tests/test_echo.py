#!/usr/bin/env python
# -*- coding: utf-8 -*-

import echo
import unittest
import subprocess
import os
import sys

# https://stackoverflow.com/questions/24722212/
# python-cant-find-module-in-the-same-folder
file_dir = os.path.dirname('./echo.py')
sys.path.append(file_dir)


class TestEcho(unittest.TestCase):

    # Test setUp()
    def setUp(self):
        self.parser = echo.create_parser()

    # Help Test
    def test_help_small(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_help_big(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "--help"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    # Upper Test

    def test_upper_small(self):
        args = ["hello world", "-u"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO WORLD")

    def test_upper_big(self):
        args = ["hello world", "--upper"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO WORLD")

    # Lower Test
    def test_lower_small(self):
        args = ["hello world", "-l"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello world")

    def test_lower_big(self):
        args = ["hello world", "--lower"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello world")

    # Title Test
    def test_title_small(self):
        args = ["hello world", "-t"]
        namespace = self.parser.parse_args(args)
        self.assertEquals(echo.main(args), "Hello World")

    def test_title_big(self):
        args = ["hello world", "--title"]
        namespace = self.parser.parse_args(args)
        self.assertEquals(echo.main(args), "Hello World")

    # Multi-Args Test
    def test_three_small(self):
        args = ["hello world", "-tul"]
        namespace = self.parser.parse_args(args)
        self.assertEquals(echo.main(args), "Hello World")


if __name__ == '__main__':
    unittest.main()
