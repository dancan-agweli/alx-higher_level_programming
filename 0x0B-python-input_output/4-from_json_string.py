#!/usr/bin/python3
""" a function that returns an object by
a JSON representation
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON rep
    """
    return json.loads(my_str)
