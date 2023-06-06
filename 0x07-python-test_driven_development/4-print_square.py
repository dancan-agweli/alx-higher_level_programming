#!/usr/bin/python3
"""
This is the "4-print_square
"""


def print_square(size):
    """prints a square with"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
