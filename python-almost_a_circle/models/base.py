#!/usr/bin/python3
"""define the module"""
import json
import os


class Base:
    """define a class Base"""
    __nb_objects_ = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects_ += 1
            self.id = Base.__nb_objects_

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return the list represented by the JSON string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        
        with open(filename, 'r') as file:
            json_string = file.read()
            list_dictionaries = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dictionaries]
