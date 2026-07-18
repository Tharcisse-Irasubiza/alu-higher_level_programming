#!/usr/bin/python3
"""Module that defines a custom list class."""


class MyList(list):
    """A class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
