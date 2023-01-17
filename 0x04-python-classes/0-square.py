#!/usr/bin/python3
"""Simple Square module.

This is a module for a class Square.

Example:
    >>> s = Square(3)
    >>> s.get_size()
    3

"""

class Square:

    """
    This is a class Square.
    """

    def __init__(self, size):

        """
        Initialize a Square object.
        Args:
            size (int): The size of the square.
        """

        self.__size = size


    def get_size(self):

        """
        Get the size of the square.
        Returns:
            int: The size of the square.
        """

        return self.__size
