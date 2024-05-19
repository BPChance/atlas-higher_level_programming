#!/usr/bin/python3
"""defines a class"""


class BaseGeometry:
    """public instance method that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
