#!/usr/bin/python3
class Square():
    """Represents a Square class object"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize size and position attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method"""
        return self.size

    @property
    def position(self):
        """Getter method for position attribute"""

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

    @position.setter
    def position(self, value):
        """Position value initalizer"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers"""
        elif not isinstance(value[0], int) or value[0] < 0 or\
                not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers"""
        else:
            self.__position = value

    def area(self):
        """Area of the square calculation"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square object"""
        if self.__size is 0:
            print()
        else:
            for idx in range(self.position[1]):
                print()
            for cidx in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
