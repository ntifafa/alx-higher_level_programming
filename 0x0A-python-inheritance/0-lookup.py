#!/usr/bin/python3
"""
module returns list of available
attributes and methods of an object

"""


def lookup(obj):
    """scans for all attributes and methods of an object"""
    return dir(obj)
