#!/usr/bin/python3
"""
Square Class creation
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class initialization"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, my_size):
        """size setter"""
        if type(my_size) is not int:
            raise TypeError("width must be an integer")
        if my_size <= 0:
            raise ValueError("width must be > 0")
        self.height = my_size
        self.width = my_size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
