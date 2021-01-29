#!/usr/bin/python3
"""
Rectangle Class Initialization
"""
:

class Rectangle(Base):
    """ """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        super().__init__(id)

    @getter
    def width(self):
        return self.__width

    @getter
    def height(self):
        return self.__height

    @getter
    def x(self):
        return self.__x

    @getter
    def y(self):
        return self.__y

    @setter
    def width(self, my_width):
        self.__width = my_width

    @setter
    def height(self, my_height):
        self.__height = my_height

    @setter
    def x(self, x_value):
        self.__x = x_value

    @setter
    def y(self, y_value):
        self.__y = y_value
