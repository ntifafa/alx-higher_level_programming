#!/usr/bin/python3
"""
module is a base class for all other classes
"""


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
