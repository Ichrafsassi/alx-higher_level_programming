#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the,
    specified class ; otherwise False"""
    return type(obj) == a_class
