#!/usr/bin/python3
"""module defines a student class"""


class Student:
    """
    represents a student class
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor for a student instance

        Args:
            @first_name: first name string
            @last_name: last name string
            @age: age string
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        converts an instance of a class
        to JSON-serializable representation
        """
        if isinstance(attrs, list) and\
                all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        return self.__dict__
