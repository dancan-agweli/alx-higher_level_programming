#!/usr/bin/python3
"""a locked class."""


class LockedClass:
    """
    Prevent the user from instantianting a class
    """

    __slots__ = ["first_name"]
