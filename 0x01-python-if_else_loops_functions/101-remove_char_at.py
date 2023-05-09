#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    a = 0

    alx = ""
    for d in str:
        if a == n:
            a += 1
            continue
        alx += str[a]
        a += 1
    return d
