#!/usr/bin/python3
"""
This is a module for a class Square
which contains a private attribute size.
"""
class Square:
"""
This is a class Square with a private attribute size.
I am not sure how to be more specific.
Trying to please the PEP8 gods.
"""
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
