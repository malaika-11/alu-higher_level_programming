#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
<<<<<<< HEAD
            print("{:02d}".format(i * 10 + j))
        else:
            print("{:02d}".format(i * 10 + j), end=", ")
=======
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}, ".format(i, j), end="")
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
