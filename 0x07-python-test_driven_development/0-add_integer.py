#!/usr/bin/python3
"""Add_integer module."""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: first argument
        b: second argument
    Returns:
        the sum of two arguments passed
    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
