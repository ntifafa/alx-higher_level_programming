#!/usr/bin/python3
"""
this module defines a function
that converts a string to JSON
"""
import json


def to_json_string(my_obj):
    """
    returns JSON representation
    of passed string object

    Args:
        @my_obj: object to be converted
    """
    return json.dumps(my_obj)
