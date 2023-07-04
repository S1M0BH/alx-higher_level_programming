#!/usr/bin/python3
"""defines rectangle (class)"""


class Rectangle:
    """ Df rectangle based on 0-rectangle.py"""

    def __init__(self, width=0, height=0):
        """Initializes this rectangle with (width-height)"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Sets height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height attribute"""""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
