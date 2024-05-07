#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = []

    for item in my_list:
        if item == search:
            replaced_list.append(replace)
        else:
            replaced_list.append(item)

    return replaced_list
