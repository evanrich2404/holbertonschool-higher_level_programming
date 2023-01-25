#!/usr/bin/python3
"""Module for matrix_divided function"""

matrixmust = "matrix must be a matrix (list of lists) of integers/floats"

def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    if type(matrix) is not list:
        raise TypeError(matrixmust)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) == 0:
        raise TypeError(matrixmust)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(matrixmust)
    return [[round(element / div, 2) for element in row] for row in matrix]
