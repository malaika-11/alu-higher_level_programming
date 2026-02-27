#!/usr/bin/python3

def uppercase(text):
    """Print a string in uppercase followed by a new line"""
    for char in text:
        # convert lowercase to uppercase
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()  # newline at the end

# Example calls
uppercase("best")
uppercase("Best School 98 Battery street")
