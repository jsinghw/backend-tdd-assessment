#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = 'jsinghw'


import argparse


def convert_upper(text):
    return(text.upper())


def convert_lower(text):
    return(text.lower())


def convert_title(text):
    return(text.title())


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
                        description='Perform transformation on input text.')
    parser.add_argument('text', action='store',
                        type=str, help='text to be manipulated')
    parser.add_argument('-u', '--upper', action="store_true", default=None,
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', default=None,
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true', default=None,
                        help='convert text to titlecase')
    args = parser.parse_args()
    return args


def main(args):
    """Implementation of echo"""
    print (args)
    output = args.text
    if args.upper is True:
        output = convert_upper(output)
    if args.lower is True:
        output = convert_lower(output)
    if args.title is True:
        output = convert_title(output)
    return output


if __name__ == '__main__':
    print(main(create_parser()))
