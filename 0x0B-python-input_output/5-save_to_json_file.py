#!/usr/bin/python3
"""
this module defines a function
that saves object to a JSON file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes and saves JSON form
    of an object text file

    Args:
        @my_obj: object text file
        @filename: name of file to be saved
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
