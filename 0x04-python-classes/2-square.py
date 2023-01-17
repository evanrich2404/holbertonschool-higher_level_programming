#!/usr/bin/python3
"""

This module is for finding area of the class Square

"""


class Square:

    """
    This class defines a Square
    """

    def __init__(self, size=0):
        """

        This method initializes the size of the square, makes sure
        it is an integer and greater than or equal to zero. Also
        setting it to private.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

            """

            assigning the size to the private instance attribute

            """

    def area(self):
        """

        This method returns the current square area

        """
        return self.__size ** 2

        """

        returning the area of the square

        """
