#!/usr/bin/python3
"""define a module"""
import json


def save_to_json_file(my_obj, filename):
    """define a function"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
