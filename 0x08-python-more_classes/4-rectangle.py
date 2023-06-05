#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:
    """a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """return attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """get attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns  string of the rectangle"""
        st = ""
        if self.__width != 0 and self.__height != 0:
            st += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return st

    def __repr__(self):
        """returns a string"""
        return "Rectangle({:d}, {:d})".format(
