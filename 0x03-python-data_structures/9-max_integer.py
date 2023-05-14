#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    x = my_list[0]
    for xx in my_list:
        if xx > x:
            x = xx
    return x
