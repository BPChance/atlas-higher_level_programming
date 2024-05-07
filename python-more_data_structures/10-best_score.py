#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_key
    return best_key
