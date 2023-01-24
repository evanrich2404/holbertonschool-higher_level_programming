#!/usr/bin/python3
"""Module 2-rectangle
Module that defines a class Rectangle
Private instance attribute: width
Private instance attribute: height
Area and Perimeter public methods
String representation of the rectangle
"""


class Rectangle:

    """Class Rectangle that defines a rectangle
    In this class we define a rectangle with private instance attributes
    We use property and setter to validate the data
    """

    def __init__(self, width=0, height=0):

        """
        Instantiation with optional width and height
        Args:
            width (int): width of a rectangle
            height (int): height of a rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """Property to retrieve width"""

        return self.__width

    @width.setter
    def width(self, value):

        """Property setter to set width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):

        """Property to retrieve height"""

        return self.__height

    @height.setter
    def height(self, value):

        """Property setter to set height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):

        """Public instance method that returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):

        """Public instance method that returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def my_str(self):

        """Public instance method that returns a string representation
        of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):

        """String representation of the rectangle to be able to recreate
        a new instance by using eval()
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)
