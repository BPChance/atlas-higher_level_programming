#!/usr/bin/python3
"""define a module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a class Square"""

    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
