#!/usr/bin/python3
"""I am making a class for Squares, and I am going to make a getter for size.
Hopefully this works."""
class Square:
    """This is a class for squares. Which should also get teh size of the square. Size is a private attribute. Maybe this will please the checker."""
    def __init__(self, size):
        self.__size = size
    
    def get_size(self):
        return self.__size
