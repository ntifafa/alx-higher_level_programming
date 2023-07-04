#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """permits the instatiation of an attribute by name first_name
    """
    __slots__ = ["first_name"]
