#!/usr/bin/python3
"""inherited list class MyList."""

class MyList(list):
    """ the built-in list class."""

    def print_sorted(self):
        """ list in sorted ascending order."""
        print(sorted(self))
