#!/usr/bin/python3
"""inherits from BaseGeometry module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines rectangle class"""
    def __init__(self, width, height):
        """constructor for Rectangle instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
