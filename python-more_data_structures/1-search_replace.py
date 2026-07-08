#!/usr/bin/python3
"""Module that defines search_replace."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list.

    Args:
        my_list (list): the initial list.
        search: the element to replace in the list.
        replace: the new element.

    Returns:
        list: a new list with all occurrences of search replaced by
        replace.
    """
    return [replace if item == search else item for item in my_list]
