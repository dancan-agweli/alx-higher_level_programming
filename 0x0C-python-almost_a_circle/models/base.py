#!/usr/bin/python3
"""

A model that contains a Base class
"""

from os import path
import json


class Base:
    """
    ...
    """

__nb_objects = 0

def __init__(self, id=None):
    """...
    """
    if id is None:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
    else:
        self.id = id

@staticmethod
def to_json_string(list_dictionaries):
    """...
    """
    if not list_dictionaries:
        return '[]'

    return json.dumps(list_dictionaries)

@classmethod
def save_to_file(cls, list_objs):
    """...
    """
    filename = cls.__name__ + '.json'

    with open(filename, mode='w', encoding='utf-8') as f:
        if not list_objs:
            return f.write(cls.to_json_string(None))

        json_attrs = [elem.to_dictionary() for elem in list_objs]
        return f.write(cls.to_json_string(json_attrs))

@staticmethod
def from_json_string(json_string):
    """...
    """
    if not json_string:
        return []

    return json.loads(json_string)

@classmethod
def create(cls, **dictionary):
    """...
    """
    if cls.__name__ == 'Square':
        dummy = cls(3)

    if cls.__name__ == 'Rectangle':
        dummy = cls(3, 3)

    dummy.update(**dictionary)
    return dummy

@classmethod
def load_from_file(cls):
    """...
    """
    filename = cls.__name__ + '.json'

    if not path.exists(filename):
        return []

    with open(filename, mode='r', encoding='utf-8') as f:
        objs = cls.from_json_string(f.read())
        instances = [cls.create(**elem) for elem in objs]
        return instances

