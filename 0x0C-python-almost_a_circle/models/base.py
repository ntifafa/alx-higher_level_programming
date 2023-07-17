#!/usr/bin/python3
"""
module is a base class for all other classes
"""
import json


class Base:
    "this class defines a base"
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a dictionary into a json string"""
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
