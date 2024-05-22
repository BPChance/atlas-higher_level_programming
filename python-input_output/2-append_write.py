#!/usr/bin/python3
"""define a module"""


def append_write(filename="", text=""):
    """define a function"""
    with open(filename, "a", encoding="utf-8") in file:
        return file.write(text)
