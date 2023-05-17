#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for y, x in sorted(a_dictionary.items()):
        if x == value:
            del a_dictionary[y]
    return a_dictionary
