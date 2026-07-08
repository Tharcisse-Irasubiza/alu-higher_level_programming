#!/usr/bin/python3
"""Module that defines safe_print_integer."""


def safe_print_integer(value):
    """Print an integer using "{:d}".format().

    Args:
        value: any type of value.

    Returns:
        bool: True if value has been correctly printed as an
        integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
