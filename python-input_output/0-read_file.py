#!/usr/bin/python3
"""define a module"""


def read_file(filename=""):
    """define a function read_file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
