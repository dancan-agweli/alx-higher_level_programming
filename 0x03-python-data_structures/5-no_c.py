#!/usr/bin/python3

def no_c(my_string):
    alx = ''
    for x in my_string:
        if x != 'c' and x != 'C':
            alx += x

    return alx
