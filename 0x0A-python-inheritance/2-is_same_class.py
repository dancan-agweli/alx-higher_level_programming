#!/usr/bin/python3
"""checking function."""


def is_same_class(obj, a_class):
    """Check for  an object is exactly an instance of a give
    """
    if type(obj) == a_class:
        return True
    return False
