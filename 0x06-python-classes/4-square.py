#!/usr/bin/python3
class Square():
    """Represents a Square class object"""
    def __init__(self, size=0):
        """Initialize size attribute"""
        self.size = size

    @size.setter
    def size(self, size=0):
        """Size data value initialization"""
        if (isinstance(size, int) is False):
            print("size must be an integer")
            raise TypeError
        elif size < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """Area of the square calculation"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter method"""
        return self.size
