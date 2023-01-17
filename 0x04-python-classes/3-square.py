#!/usr/bin/python3
"""
This module uses a setter and a getter to set and get the size of a
class Square
"""


class Square:

    """
    This class defines a Square with a private instance attribute
    """

    def __init__(self, size=0):

        """
        This function initializes the Square class
        """

        self.size = size

    @property
    def size(self):

        """
        This function retrieves the size of the Square using getter
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        This function uses a setter to set the size of the Square
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """
        This function returns the area of the Square
        """

        return self.__size ** 2
