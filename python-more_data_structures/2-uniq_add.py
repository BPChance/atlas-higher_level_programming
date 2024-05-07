#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()

    for num in my_list:
        unique_integers.add(num)

    return sum(unique_integers)
