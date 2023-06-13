#!/usr/bin/python3
""" class Student
"""


class Student:
    """ create student instances """

    def __init__(self, first_name, last_name, age):
        """ method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d[satr] = obj[satr]
            return d

        return obj
