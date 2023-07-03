#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize an instance of a rectangle
        Args:
            width - refers to the width of the rectangle
            height - refers to the height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Retrives private instance attribute"""
        return(self.__width)

    @width.setter
    def width(self, val):
        """Sets private instance attribute
        Raises:
            TypeError - when value passed is not an integer
            ValueError - when value passed is less than 0
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = val

    @property
    def height(self):
        """Retrives private instance attribute"""
        return(self.__height)

    @height.setter
    def height(self, val):
        """"Sets private instance attribute
        Raises:
            TypeError - when value passed is not an integer
            ValueError - when value passed is less than 0
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = val

    def area(self):
        """"Computes the area of a rectangle"""
        return(self.__width * self.__height)

    def perimeter(self):
        """"Computes the perimeter of a rectangle"""
        return((self.__width + self.__height) * 2)
