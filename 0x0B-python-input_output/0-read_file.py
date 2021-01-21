#!/usr/bin/python3
""" Opens a dile to read """


def read_file(filename=""):
    """ Opens and reads a file in UTF-8 """
    with open(filename, "r", encoding="utf-8") as holder:
        print(holder.read(), end="")
