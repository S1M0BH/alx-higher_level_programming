#!/usr/bin/python3
"""defines a square on square"""


class Square:
    """Substitute square"""

    def __init__(self, size=0):
        """Initialize for data"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
