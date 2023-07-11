#!/usr/bin/python3
"""
this module defines a function
that reads an existing file
"""


def read_file(filename=""):
    """
    read_file - open file, read, print to stdout and close

    Args:
        @filename: name of file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
