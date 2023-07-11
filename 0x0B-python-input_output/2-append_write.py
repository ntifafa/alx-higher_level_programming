#!/usr/bin/python3
"""
this module defines a function that
creates and appends to a file
"""


def append_write(filename="", text=""):
    """
    create file, append string to text
    file upon each call and close

    Args:
        @filename: name of file
        @text: text to be written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
