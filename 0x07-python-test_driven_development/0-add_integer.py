#!/usr/bin/python3
"""Add_integer module."""


def add_integer(a, b=98):
    """Adds two integers"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
