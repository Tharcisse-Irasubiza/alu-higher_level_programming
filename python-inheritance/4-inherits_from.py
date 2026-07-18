#!/usr/bin/python3
"""Module that checks class inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance_class."""
    return isinstance(obj, a_class) and type(obj) != a_class
