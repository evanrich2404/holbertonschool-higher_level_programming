#!/usr/bin/python3
"""

This module contains a function that adds two integers.
a and b must be integers or floats, otherwise raise a TypeError exception with
the message a must be an integer or b must be an integer.
a and b must be first casted to integers if they are float.
Returns an integer: the addition of a and b.
You are not allowed to import any module
the defined prototype: def add_integer(a, b=98):

"""


def add_integer(a, b=98):
    """
    This function adds two integers.
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
