#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(object, attr_name, value):
    """Adds a new attribute to an object if it's possible."""
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)
