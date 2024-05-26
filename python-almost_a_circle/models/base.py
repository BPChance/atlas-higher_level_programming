#!/usr/bin/python3
"""define the module"""


class Base:
    """define a class Base"""
    __nb_objects_ = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects_ += 1
            self.id = Base.__nb_objects_
