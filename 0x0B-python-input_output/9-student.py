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

    def to_json(self):
        """
        retrieves a dictionary representation
        of a Student instance
        """
        return self.__dict__
