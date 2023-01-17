#!/usr/bin/python3
"""I am making a class for Squares, and I am going to make a getter for size.
Hopefully this works."""
class Square:
    def __init__(self, size):
        """Initializing the size"""
        self.__size = size
    
    def get_size(self):
        """And now getting the size"""
        return self.__size
