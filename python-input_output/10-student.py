#!/usr/bin/python3
"""Module defining Student class with filtering."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary of selected attributes."""
        if isinstance(attrs, list):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__
