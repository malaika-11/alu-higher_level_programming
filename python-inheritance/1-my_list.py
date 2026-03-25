#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """
    A subclass of list with added sorting functionality.

    >>> my_list = MyList([1, 4, 2, 3, 5])
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original.

        >>> my_list = MyList([10, -5, 0, 3])
        >>> my_list.print_sorted()
        [-5, 0, 3, 10]
        """
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
