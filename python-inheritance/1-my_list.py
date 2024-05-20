#!/usr/bin/python3
"""define a class"""


class MyList(list):
    """print list in ascending order"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
