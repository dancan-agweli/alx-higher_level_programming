#!/usr/bin/python3
"""function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
