#!/usr/bin/python3
"""
this module contains a function that returns True if the object is an instance
and False if not
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class and False if not
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
