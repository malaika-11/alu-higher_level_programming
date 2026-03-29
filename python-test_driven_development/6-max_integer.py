#!/usr/bin/python3
"""Module that provides max_integer function."""


def max_integer(list=[]):
    """Return the maximum integer in a list, or None for empty lists."""
    if len(list) == 0:
        return None

    result = list[0]
    for value in list:
        if value > result:
            result = value
    return result
