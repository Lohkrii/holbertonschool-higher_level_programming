#!/usr/bin/python3
def uppercase(str):
    for idx in str:
        holder = ord(idx)
        if idx.islower():
            holder -= 32
        print("{:c}".format(holder), end="")
    print()
