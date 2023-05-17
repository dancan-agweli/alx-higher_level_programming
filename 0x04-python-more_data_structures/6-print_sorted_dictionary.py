#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary.items())
    for m, n in x:
        print('{0}: {1}'.format(m, n)
