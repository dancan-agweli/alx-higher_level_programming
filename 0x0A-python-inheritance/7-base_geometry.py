#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """An instance methods area and integer_validator"""
    def area(self):
        """raises an exception on  calling"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
