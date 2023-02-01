#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square subclass of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        holder = "[Square] " + "({}) ".format(self.id)
        holder += "{}/{} - ".format(self.x, self.y)
        holder += "{}".format(self.width)
        return holder

    def update(self, *args, **kwargs):
        """update square args"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dictionary representation"""
        holddeez = {"id": self.id,
                    "size": self.width, "x": self.x, "y": self.y}
        return holddeez
