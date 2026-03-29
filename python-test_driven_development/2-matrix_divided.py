#!/usr/bin/python3
"""Module that provides a function to divide matrix values."""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by div."""
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(error)

    if len(matrix) == 0:
        raise TypeError(error)

    if any(not isinstance(row, list) for row in matrix):
        raise TypeError(error)

    if any(len(row) == 0 for row in matrix):
        raise TypeError(error)

    for row in matrix:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(error)

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
