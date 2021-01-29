#!/usr/bin/python3
"""
Initializing Class: Base
"""


class Base():
    """ Base class initialization """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Attribute initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
