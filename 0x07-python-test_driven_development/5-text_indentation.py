#!/usr/bin/python3
"""
This is the "5-test_indentation
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    for b in text:
        if x == 0:
            if b == ' ':
                continue
            else:
                x = 1
        if x == 1:
            if b == '?' or b == '.' or b == ':':
                print(b)
                print()
                x = 0
            else:
                print(b, end="")
