#!/usr/bin/python3
def fizzbuzz():
<<<<<<< HEAD
=======
    """Print numbers from 1 to 100 with Fizz/Buzz rules"""
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
<<<<<<< HEAD
=======
    print()
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
