#!/usr/bin/python3
class Square():
    """Represents a square object"""
    def __init__(self, size=0):
        """Size data value initialization"""
        if (isinstance(size, int) is False:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
