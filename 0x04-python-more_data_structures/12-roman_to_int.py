#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    diction = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    x = 0

    for y in range(len(roman_string)):
        if diction.get(roman_string[y], 0) == 0:
            return (0)
        if (y != (len(roman_string) - 1) and
                diction[roman_string[y]] < diction[roman_string[y + 1]]):
                x += diction[roman_string[y]] * -1

        else:
            x += diction[roman_string[y]]
    return (x)
