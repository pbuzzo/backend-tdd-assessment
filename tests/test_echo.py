#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


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
        args = ["hello", "-u"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")

    def test_upper_big(self):
        args = ["hello", "--upper"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")

    # Lower Test
    def test_lower_small(self):
        args = ["hello", "-l"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello")

    def test_lower_big(self):
        args = ["hello", "--lower"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello")

    # Title Test
    def test_title_small(self):
        args = ["hello", "-t"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.capitalize)
        self.assertEquals(echo.main(args), "Hello")

    def test_title_big(self):
        args = ["hello", "--title"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.capitalize)
        self.assertEquals(echo.main(args), "Hello")

    # Multi-Args Test
    def test_three_small(self):
        args = ["hello", "-tul"]
        namespace = self.parser.parse_args(args)
        pass

    def test_two_small(self):
        args = ["hello", "-ul"]
        namespace = self.parser.parse_args(args)
        pass

    # Test tearDown()
    def tearDown(self):
        self.parser.tearDown()
        self.parser = None


if __name__ == '__main__':
    unittest.main()
