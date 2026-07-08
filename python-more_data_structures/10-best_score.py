#!/usr/bin/python3
"""Module that defines best_score."""


def best_score(a_dictionary):
    """Return the key with the biggest integer value.

    Args:
        a_dictionary (dict): dictionary whose values are all
        integers.

    Returns:
        The key associated with the highest value, or None if
        a_dictionary is empty, None, or otherwise falsy.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
