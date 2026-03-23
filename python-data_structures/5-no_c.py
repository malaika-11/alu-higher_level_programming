#!/usr/bin/python3


def no_c(my_string):
    result = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            result = result + my_string[i]
    return result
