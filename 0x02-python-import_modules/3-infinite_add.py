#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    add = 0
    for idx in argv[1:]:
        add += int(idx)
    print(add)
