#!/usr/bin/python3
"""find the max integer in a list
"""


def max_integer(list=[]):
    """ return the max integer in a list of integers
    """
    if len(list) == 0:
        return None
    ret = list[0]
    x = 1
    while x < len(list):
        if list[x] > ret:
            ret = list[x]
        x += 1
    return 
