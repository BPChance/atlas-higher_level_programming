#!/usr/bin/python3
"""defines a class"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        def area(self):
            return self.__size * self.__size
