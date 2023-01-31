#!/usr/bin/python3
"""module 12-pascal_triangle.py"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascal = [[1], [1, 1]]
    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        row.append(1)
        pascal.append(row)
    return pascal
