#!/usr/bin/python3
<<<<<<< HEAD
print(", ".join("{:02d}".format(i) for i in range(100)))
=======
for i in range (0, 100):
    if i != 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
