#!/usr/bin/python3
"""Module that defines safe_print_list."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): list containing any type of elements.
        x (int): number of elements to print. Can be bigger than
        the length of my_list.

    Returns:
        int: the real number of elements printed.
    """
    nb_print = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            nb_print += 1
        except IndexError:
            break
    print()
    return nb_print
