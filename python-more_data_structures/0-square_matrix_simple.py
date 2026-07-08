#!/usr/bin/python3
"""Module that defines square_matrix_simple."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix.

    Args:
        matrix (list of list of int): the 2D matrix to square.

    Returns:
        list of list of int: a new matrix, same size as matrix, where
        each value is the square of the corresponding input value.
    """
    return [[value ** 2 for value in row] for row in matrix]
