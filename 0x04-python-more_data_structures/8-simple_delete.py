#!/usr/bin/python3
def simple_delete(my_dictionary, key=""):
    if key in my_dictionary:
        del my_dictionary[key]
    return my_dictionary
