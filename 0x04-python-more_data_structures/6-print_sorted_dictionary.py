#!/usr/bin/python3
def print_sorted_dictionary(my_dictionary):
    keys = []
    if my_dictionary:
        for k, idx in my_dictionary.items():
            keys.append(k)

        keys.sort()
        for k in keys:
            print("{}: {}".format(k, my_dictionary[k]))
