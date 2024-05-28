#!/usr/bin/python3
"""define a module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        #self.__validate_integer("size", value)
       # self.__validate_positive("size", value)
        self.width = value
        self.height = value

    def area(self):
        """returns area of square"""
        return self.width ** 2

    # update method
    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # dictionary method
    def to_dictionary(self):
        """return dictionary representation of square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    # validation methods
    def __validate_integer(self, name, value):
        """check if is integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def __validate_positive(self, name, value):
        """check if integer is positive"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
