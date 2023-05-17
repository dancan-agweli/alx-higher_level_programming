#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, x in sorted(a_dictionary.items()):
        print(key, x, sep=': ')
