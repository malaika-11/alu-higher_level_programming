#!/usr/bin/python3
<<<<<<< HEAD
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
=======
def uppercase(text):
    """Print a string in uppercase followed by a new line"""
    for char in text:
        # convert lowercase to uppercase
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print()  # newline at the end
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
