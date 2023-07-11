#!/usr/bin/python3
"""
this module defines a function
that creates and writes to file
"""


def write_file(filename="", text=""):
    """
    write_file - pass string to text file

    Args:
        @filename: name of file
        @text: text to be written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
