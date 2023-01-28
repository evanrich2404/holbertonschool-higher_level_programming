#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """This class defines a base geometry"""
    def area(self):
        """This method raises an exception"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """This method validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
