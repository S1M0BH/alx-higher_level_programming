#!/usr/bin/python3
"""This module inherits from list class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """print a sorted list"""

        print(sorted(self))
