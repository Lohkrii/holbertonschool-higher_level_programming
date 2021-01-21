#!/usr/bin/python3
""" Appends string to end of text file """


def append_write(filename="", text=""):
    """ Appends string to file """
    with open(filename, "a", encoding="utf-8") as holder:
        return holder.write(text)
