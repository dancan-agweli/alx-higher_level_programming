#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    x = a_dictionary.copy()
    for m, n in x.items():
        x[m] = n * 2

    return x
