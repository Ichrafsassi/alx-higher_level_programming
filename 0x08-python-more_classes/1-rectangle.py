#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width : The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """GET/SET the width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """GET/SET the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
