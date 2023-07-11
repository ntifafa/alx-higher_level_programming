#!/usr/bin/python3
"""
this module defines a function that
converts a JSON string to an object
"""
import json


def from_json_string(my_str):
    """
    returns an object derived
    from a JSON string

    Args:
        @my_str: string to be converted
    """
    return json.loads(my_str)
