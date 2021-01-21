#!/usr/bin/python3
""" Json class """


def class_to_json(obj):
    """Returns dictionary description with simple data structure """
    new_dict = obj.__dict__
    return new_dict
