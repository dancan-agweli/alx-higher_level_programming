#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        data = fct(*args)

    except ZeroDivisionError:
        data = None
        sys.stderr.write("Exception: division by zero\n")
    except IndexError:
        data = None
        sys.stderr.write("Exception: list index out of range\n")

    return data
