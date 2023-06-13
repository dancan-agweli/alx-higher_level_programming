#!/usr/bin/python3
""" function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line 

    """

    res = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res += [line]
            if line.find(search_string) != -1:
                res += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res))
