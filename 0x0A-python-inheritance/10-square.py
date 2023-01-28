#!/usr/bin/python3
""" This module contains a function that creates a square class that
inherits from Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle class
    """
    def __init__(self, size):
        """ This method initializes the class
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ This method returns the area of the square
        """
        return self.__size ** 2

