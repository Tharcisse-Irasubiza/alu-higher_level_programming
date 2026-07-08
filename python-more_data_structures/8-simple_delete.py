#!/usr/bin/python3
"""Module that defines simple_delete."""


def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.

    Args:
        a_dictionary (dict): the dictionary to update.
        key (str): the key to delete. If it doesn't exist, the
        dictionary is left unchanged.

    Returns:
        dict: the updated dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
