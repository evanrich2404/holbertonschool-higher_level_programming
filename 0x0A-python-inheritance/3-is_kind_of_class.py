#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an instance
and False if not
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance and False if not"""
    return isinstance(obj, a_class)
