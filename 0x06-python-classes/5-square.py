#!/usr/bin/python3
"""defines a square on square """


class Square:
    """Substitute square"""

    def __init__(self, size=0):
        """Initializes for data """

        self.__size = size

    @property
    def size(self):
        """Retrieves size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """print square in (#) """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
    
    
    def area(self):
        """Return square area """

        return (self.__size ** 2)
