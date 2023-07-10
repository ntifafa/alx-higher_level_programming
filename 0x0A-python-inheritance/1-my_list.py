#!/usr/bin/python3
"""
module inherits from a list and
prints in an ascending order
"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        """prints list in an asc order"""
        print(sorted(self))
