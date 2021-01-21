#!/usr/bin/python3
""" Verifies if object is inherited of a specified class. """

def inherits_from(obj, a_class):
    """ Check if class of obj is of specified class """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
