#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class"""
    return type(obj) is a_class
