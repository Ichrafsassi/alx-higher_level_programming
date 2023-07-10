#!/usr/bin/python3
"""Defines a class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """Class BaseGeometry."""
    def area(self):
        """Area function."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
