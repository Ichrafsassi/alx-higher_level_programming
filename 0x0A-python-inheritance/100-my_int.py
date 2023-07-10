#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """Defines a class MyInt """
    def __init__(self, value):
        """Creates new instances of class MyInt."""
        self.__value = value

    def __eq__(self, other):
        """The method equal"""
        return self.__value != other

    def __ne__(self, other):
        """The method not equal"""
        return self.__value == other
