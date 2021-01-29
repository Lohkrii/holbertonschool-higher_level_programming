#!/usr/bin/python3
"""
Rectangle Class Initialization
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class and values initializations
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class initialization and value assignment"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width getter """
        return self.__width

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, my_width):
        """Width Setter and checks for edge cases"""
        if type(my_width) is not int:
            raise TypeError("width must be an integer")
        if my_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = my_width

    @height.setter
    def height(self, my_height):
        """Height setter and checks for edge cases"""
        if type(my_height) is not int:
            raise TypeError("height must be an integer")
        if my_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = my_height

    @x.setter
    def x(self, x_value):
        """x setter and checks for edge cases"""
        if type(x_value) is not int:
            raise TypeError("x must be an integer")
        if x_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_value

    @y.setter
    def y(self, y_value):
        """y setter and checks for edge cases"""
        if type(y_value) is not int:
            raise TypeError("y must be an integer")
        if y_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_value
