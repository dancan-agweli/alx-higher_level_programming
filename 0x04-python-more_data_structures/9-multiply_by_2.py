#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    fresh = a_dictionary.copy()
    for y, x in list(fresh.items()):
        fresh[y] = x * 2
    return fresh
