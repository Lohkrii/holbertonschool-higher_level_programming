#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        count_arg = "argument:"
    elif len(argv) < 2:
        count_arg = "arguments."
    else:
        count_arg = "arguments:"
    print("{} {}".format(len(argv) - 1, count_arg))
    for idx in range(1, len(argv)):
        print("{}: {}".format(idx, argv[idx]))
