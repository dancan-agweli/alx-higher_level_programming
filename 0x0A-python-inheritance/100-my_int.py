#!/usr/bin/python3
"""
 class MyInt
"""


class MyInt(int):
    """ an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """ new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """current"""
        return int(self) != other

    def __ne__(self, other):
        """current="""
        return int(self) == other
