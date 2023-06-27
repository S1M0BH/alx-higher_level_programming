#!/usr/bin/python3
"""defines a square on square"""


class Square:
    """Substitute square"""
    def __init__(self, size=0):
        """Initializing for data """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ Return the square area """

        return (self.__size * self.__size)
