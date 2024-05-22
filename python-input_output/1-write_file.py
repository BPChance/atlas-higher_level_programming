#!/usr/bin/python3
"""define a module"""


def write_file(filename="", text=""):
    """define a function"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
