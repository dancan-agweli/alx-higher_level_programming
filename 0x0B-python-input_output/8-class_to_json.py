#!/usr/bin/python3
""" Module that returns the dictionary
"""


def class_to_json(obj):
    """retuns the dictionary description of an obj """

    x = {}
    if hasattr(obj, "__dict__"):
        x = obj.__dict__.copy()
    return x
