#!/usr/bin/python3
def multiple_returns(sentence):

    if len(sentence) == 0:
        alx = len(sentence), None
        return alx
    alx = len(sentence), sentence[0]
    return alx
