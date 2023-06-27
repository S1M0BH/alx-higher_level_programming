#!/usr/bin/python3
"""defines a square on square"""


class Square:
    """Substitute square"""

    def __init__(self, size=0):
        """Initializing for data """

        self.size = size

    @property
    def size(self):
        """Retrieves size square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set Size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Return the square area"""

        return (self.__size * self.__size)
