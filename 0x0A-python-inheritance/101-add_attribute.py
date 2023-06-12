#!/usr/bin/python3
""" add """


def add_attribute(ddObject, ddName, ddValue):
    """ add_attribute function """
    if not hasattr(ddObject, "__dict__"):
        raise TypeError("can't add new attribute")
    if (not hasattr(ddObject, ddName)):
        ddObject.__setattr__(ddName, ddValue)
