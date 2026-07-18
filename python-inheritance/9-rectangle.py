#!/usr/bin/python3
"""Module that defines a complete Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with area calculation."""

    def __init__(self, width, height):
        """Initialize rectangle dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
