#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    a = list(a_dictionary.keys())[0]
    b = a_dictionary[ret]
    for m, n in a_dictionary.items():
        if n > b:
            b = n
            a = m
    return (a)
