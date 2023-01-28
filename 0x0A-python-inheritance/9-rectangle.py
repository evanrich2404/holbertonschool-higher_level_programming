#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from BaseGeometry
It also contains a class method that validates the value of width and height
and a class method that returns the area of the rectangle
It should print, and should be able to handle ValueError and TypeError
str() should return
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherits from BaseGeometry"""
    def __init__(self, width, height):
        """This class method validates the value of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This class method returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This class method returns a string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
