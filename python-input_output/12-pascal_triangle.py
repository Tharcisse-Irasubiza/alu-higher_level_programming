#!/usr/bin/python3
"""Module for generating Pascal's triangle."""


def pascal_triangle(n):
    """Returns Pascal's triangle with n rows."""
    triangle = []

    if n <= 0:
        return triangle

    for row in range(n):
        current = [1] * (row + 1)

        for i in range(1, row):
            current[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]

        triangle.append(current)

    return triangle
