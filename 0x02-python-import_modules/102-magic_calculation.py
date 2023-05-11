#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if (a < b):
        x = add(a, b)

        for y in range(4, 6):
            x = add(x, y)

        return x
    else:
        return sub(a, b)
