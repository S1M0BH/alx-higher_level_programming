#!/usr/bin/python3
"""Defines a square print func """


def print_square(size):
    """Print a square with the char """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
