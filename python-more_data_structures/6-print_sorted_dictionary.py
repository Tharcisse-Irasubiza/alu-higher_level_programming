#!/usr/bin/python3
"""Module that defines print_sorted_dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys.

    Args:
        a_dictionary (dict): the dictionary to print. All keys are
        assumed to be strings. Only the first level of keys is
        sorted.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
