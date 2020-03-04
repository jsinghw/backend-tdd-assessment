#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    # Test if convert_upper returns uppercase string
    def test_upper(self):
        self.assertIsNotNone(echo.convert_upper)
        self.assertEquals(echo.convert_upper('hello'), 'HELLO')
        self.assertEquals(echo.convert_upper('Yo'), 'YO')
        self.assertEquals(echo.convert_upper("It's a me."), "IT'S A ME.")

    # Test if conver_lower returns lowercase string
    def test_lower(self):
        self.assertIsNotNone(echo.convert_lower)
        self.assertEquals(echo.convert_lower('HELLo'), 'hello')
        self.assertEquals(echo.convert_lower('Yo'), 'yo')
        self.assertEquals(echo.convert_lower("It's a me."), "it's a me.")

    # Test if convert_title returns title string
    def test_title(self):
        self.assertIsNotNone(echo.convert_title)
        self.assertEquals(echo.convert_title('hellO'), 'Hello')
        self.assertEquals(echo.convert_title('yO'), 'Yo')
        self.assertEquals(echo.convert_title('TEst'), 'Test')

    # Test if multiple options properly manipulate string
    def test_multiple_options(self):
        self.assertEquals(
            echo.main(Namespace(lower=True, text='heLLo!', title=True,
                                upper=True)), "Hello!")
        self.assertEquals(
            echo.main(Namespace(lower=True, text='heLLo!', title=None,
                                upper=True)), "hello!")
        self.assertEquals(
            echo.main(Namespace(lower=None, text='heLLo!', title=True,
                                upper=True)), "Hello!")
        self.assertEquals(
            echo.main(Namespace(lower=True, text='meLLo!', title=True,
                                upper=None)), "Mello!")

    # Test if no options are given
    def test_no_args(self):
        self.assertIsNotNone(echo.main)
        self.assertEquals(
            echo.main(Namespace(lower=None, text='test', title=None,
                                upper=None)), "test")
        self.assertEquals(
            echo.main(Namespace(lower=None, text='word', title=None,
                                upper=None)), "word")
        self.assertEquals(
            echo.main(Namespace(lower=None, text='HelLO', title=None,
                                upper=None)), "HelLO")


if __name__ == '__main__':
    unittest.main()
