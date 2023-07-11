#!/usr/bin/python3
"""Defines a func that adds attributes to objects"""


def add_attribute(obj, att, value):
    """This func add attributes to objects"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
