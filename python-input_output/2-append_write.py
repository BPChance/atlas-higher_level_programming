#!/usr/bin/python3
"""define a module"""


def append_write(filename="", text=""):
    """define a function"""
    with open(filename, "a", encoding="utf-8") as file:
        chars_added = file.write(text)
        return chars_added
