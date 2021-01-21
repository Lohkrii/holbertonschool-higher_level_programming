#!/usr/bin/python3
""" Compares an object """


def is_same_class(obj, a_class):
    """ Checks if object is of a given class """
    if type(obj) is a_class:
        return True
    else:
        return False
