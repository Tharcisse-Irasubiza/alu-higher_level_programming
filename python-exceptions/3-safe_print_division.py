#!/usr/bin/python3
"""Module that defines safe_print_division."""


def safe_print_division(a, b):
    """Divide 2 integers and print the result.

    Args:
        a (int): the dividend.
        b (int): the divisor.

    Returns:
        float: the result of the division, or None if the division
        could not be performed.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
