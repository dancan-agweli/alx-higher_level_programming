#!/usr/bin/python3
"""
This is matrix manipulation
"""


def matrix_divided(matrix, div):
    """Division pf all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "Matrix must be a matrix (list of lists) of integers/floats")
    t = None
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if t is None:
            t = len(i)
        elif t != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in i] for i in matrix]
