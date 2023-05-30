#!/usr/bin/python3
"""a class MagicClass"""
import math


class MagicClass:
    """ a circle"""
    def __init__(self, radius=0):
        """value the Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """the circumference of the circle"""
        return 2 * math.pi * self.__radius
