#!/usr/bin/python3
"""
module defines a function
that converts a class to JSON
"""


def class_to_json(obj):
    """returns a simple dictionary representation"""
    return obj.__dict__
