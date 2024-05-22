#!/usr/bin/python3
"""define a module"""
import json


def save_to_json_file(my_obj, filename):
    """define a function"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
