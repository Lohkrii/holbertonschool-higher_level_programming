#!/usr/bin/python3
"""
Rectangle Class Initialization
"""
from models.base import Base

class Rectangle(Base):
    """Rectangle Class and values initializations """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class initialization and value assignment"""
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
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

    @setter
    def width(self, my_width):
        """Width Setter"""
        self.__width = my_width

    @setter
    def height(self, my_height):
        """Height setter"""
        self.__height = my_height

    @setter
    def x(self, x_value):
        """x setter"""
        self.__x = x_value

    @setter
    def y(self, y_value):
        """y setter"""
        self.__y = y_value
