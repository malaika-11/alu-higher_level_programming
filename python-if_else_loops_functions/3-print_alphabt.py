#!/usr/bin/python3
<<<<<<< HEAD
for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end="")
=======
print("{}".format("".join(chr(i) for i in range(97, 123) if i != 101 and i != 113)), end="")
>>>>>>> d5fbd48212734c32b46a2b12b6103cfd76564c24
