#!/usr/bin/python3
"""Module that provides a function to print a square."""


def print_square(size):
    """Print a square with the character # using the provided size."""
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and not size.is_integer():
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)
    for _ in range(size):
        print("#" * size)
