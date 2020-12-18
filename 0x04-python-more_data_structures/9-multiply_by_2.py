#!/usr/bin/python3
def multiply_by_2(my_dictionary):
    new_dictionary = dict(my_dictionary)
    for key, value in my_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictrionary
