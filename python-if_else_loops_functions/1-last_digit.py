#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD

last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
=======
last_digit = number % 10
if number < 0 and last_digit != 0:
    last_digit -= 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
