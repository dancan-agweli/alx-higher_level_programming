#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """ peak in a list of unsorted integers"""
    x = list_of_integers
    l = len(x)
    if l == 0:
        return
    w = l // 2
    if (w == l - 1 or x[w] >= x[w + 1]) and (w == 0 or x[w] >= x[w - 1]):
        return x[w]
    if w != l - 1 and x[w + 1] > x[w]:
        return find_peak(x[w + 1:])
    return find_peak(x[:w])
