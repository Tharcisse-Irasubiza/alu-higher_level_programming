#!/usr/bin/python3
"""Module that defines multiply_by_2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): dictionary whose values are all
        integers.

    Returns:
        dict: a new dictionary with the same keys, where each value
        is twice the corresponding value in a_dictionary.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
