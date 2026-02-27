#!/usr/bin/python3
def pow(a, b):
<<<<<<< HEAD
    if b == 0:
        return 1
    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result
=======
    return a ** b
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
