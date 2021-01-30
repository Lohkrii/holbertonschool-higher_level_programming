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

    def update(self, *args, **kwargs):
        """Update Attributes"""
        if not args and not kwargs:
            return
        if len(args) != 0:
            my_att_list = ["id", "size", "x", "y"]
            for idx, attr in enumerate(args):
                setattr(self, att_list[idx], attr)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """return the object as a dictionar"""
        my_dict = {}
        my_att_list = ["id", "size", "x", "y"]
        for key in my_att_list:
            value = getattr(self, key)
            new_dict[key] = value
        return my_dict
