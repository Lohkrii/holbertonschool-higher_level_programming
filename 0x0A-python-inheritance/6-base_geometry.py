#!/usr/bin/python3
""" Exception raiser of inherited class """


class BaseGeometry:
    """BaseGeometry"""
    def area(self):
        """ Exception raiser """
        raise Exception("area() is not implemented")
