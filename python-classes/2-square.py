#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a Square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
