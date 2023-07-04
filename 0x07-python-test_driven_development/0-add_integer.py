#!/usr/bin/python3
"""add 2 integers module"""


def add_integer(a, b=98):
    """ Returns an integer: the addition of a and b
    Arges:
        a, b : integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
