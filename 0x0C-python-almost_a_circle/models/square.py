#!/usr/bin/python3
"""
Square Class creation
"""
from models import Base
from models import Rectangle


class Square():
    """Class initialization"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, my_size):
        self.height and self.width = my_size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

