#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize an instance of a square

        Args:
            size - is the size of the square
            and defaults to 0 if nothing is passed.
            Must be an integer not less than 0."""

        self.__size = size

    def area(self):
        """Computes and returns the area of the square

        Returns:
            Area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def size(self):
        """Retrieves private instance attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets private instance attribute.
        Raises:
            TypeError - when size passed is not an integer.
            ValueError - when size is less than 0."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
