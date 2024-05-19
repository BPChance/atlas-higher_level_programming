#!/usr/bin/python3
"""define a module"""


def inherits_from(obj, a_class):
    """define a function"""
    return isinstance(obj, a_class) and type(obj) is not a_class
