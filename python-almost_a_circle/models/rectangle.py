#!/usr/bin/python3
"""defines a module"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    # height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_integer("height", value)
        self.__validate_positive("height", value)
        self.__height = value

    # x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_integer("x", value)
        self.__validate_non_negative("x", value)
        self.__height = value

    # y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_integer("x", value)
        self.__validate_non_negative("x", value)
        self.__height = value

    # rectangle area
    def area(self):
        self.width * self.height

    # displays rectangle
    def display(self):
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + '#' * self.width)

    # override str method
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    # dictionary method
    """attributes of rectangle"""
    def to_dictionary(self):
        return{
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    # update method
    def update(self, *args, **kwargs):
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    # validation methods
    def __validate_integer(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def __validate_positive(self, name, value):
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def __validate_non_negative(self, name, value):
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
