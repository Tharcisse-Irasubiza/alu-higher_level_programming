#!/usr/bin/python3
"""Module that defines safe_print_list_integers."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list, only integers.

    Args:
        my_list (list): list containing any type of elements.
        x (int): number of elements to access in my_list. If x is
        bigger than the length of my_list, an exception is expected
        to occur and propagate.

    Returns:
        int: the real number of integers printed.
    """
    nb_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
        except (TypeError, ValueError):
            continue
    print()
    return nb_print
