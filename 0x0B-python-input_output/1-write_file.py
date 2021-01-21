#!/usr/bin/python3
""" Writes a string to a text file and returns the characters written """


def write_file(filename="", text=""):
    """ Opens file and writes string to it. Returns number of characters """
    with open(filename, "w", encoding="utf-8") as holder:
        return holder.write(text)
