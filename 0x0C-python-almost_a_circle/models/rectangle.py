#!/usr/bin/python3
"""
model calss
"""

from models.base import Base


class Rectangle(Base):
    """
    class rectangele
    """
def __init__(self, width, height, x=0, y=0, id=None):
    """
    ...
    """
    super().__init__(id)

    self._validate_integer_parameter(width, 'width')
    self._validate_integer_parameter(height, 'height')
    self._validate_integer_parameter(x, 'x')
    self._validate_integer_parameter(y, 'y')

    self._width = width
    self._height = height
    self._x = x
    self._y = y

@property
def width(self):
    """
    ...
    """
    return self._width

@width.setter
def width(self, param):
    """
    ...
    """
    self._validate_integer_parameter(param, 'width')

    self._width = param

@property
def height(self):
    """
    ...
    """
    return self._height

@height.setter
def height(self, param):
    """
    ...
    """
    self._validate_integer_parameter(param, 'height')

    self._height = param

@property
def x(self):
    """
    ...
    """
    return self._x

@x.setter
def x(self, param):
    """
    ...
    """
    self._validate_integer_parameter(param, 'x')

    self._x = param

@property
def y(self):
    """
    ...
    """
    return self._y

@y.setter
def y(self, param):
    """
    ...
    """
    self._validate_integer_parameter(param, 'y')

    self._y = param

def _validate_integer_parameter(self, value, param):
    """
    ...
    """
    if type(value) is not int:
        raise TypeError(param + ' must be an integer')

    if value <= 0 and param in ('width', 'height'):
        raise ValueError(param + ' must be > 0')

    if value < 0 and param in ('x', 'y'):
        raise ValueError(param + ' must be >= 0')

def area(self):
    """
    ...
    """
    return self._width * self._height

def display(self):
    """
    ...
    """
    if self._y > 0:
        print('\n' * self._y, end='')

    for i in range(self.height):
        if self._x > 0:
            print(' ' * self._x, end='')

        print('#' * self._width)

def __str__(self):
    """
    ...
    """
    return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
        self.id, self.x, self.y, self.width, self.height
    )

def update(self, *args, **kwargs):
    """
    ...
    """
    argc = len(args)
    kwargc = len(kwargs)
    modif_attrs = ['id', 'width', 'height', 'x', 'y']

    if argc > 5:
        argc = 5

    if argc > 0:
        for i in range(argc):
            setattr(self, modif_attrs[i], args[i])
    elif kwargc > 0:
        for k, v in kwargs.items():
            if k in modif_attrs:
                setattr(self, k, v)

def to_dictionary(self):
    """
    ...
    """
    return {
        'id': self.id,
        'width': self.width,
        'height': self.height,
        'x': self.x,
        'y': self.y
    }

