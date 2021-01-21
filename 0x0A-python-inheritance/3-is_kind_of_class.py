#!/usr/bin/python3
""" Verifies if object is of a specified class"""

def is_kind_of_class(obj, a_class):
    """ Verifies object is of specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
