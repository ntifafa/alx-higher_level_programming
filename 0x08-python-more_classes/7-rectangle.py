#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """"Represents a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """"Initializes an instance of a rectangle
        Args:
            width - refers to the width of the rectangle
            height - refers to the height of the rectangle
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves private instance attribute"""
        return self.__width

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
        """Retrieves private instance attribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """Sets private instance attribute
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
        """Computes the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Computes the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Prints the actual representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += str(self.print_symbol)
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Reproduce a string form of an object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Detects instance deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
