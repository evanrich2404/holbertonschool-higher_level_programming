#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    max = 0
    for i in a_dictionary:
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            name = i
    return name
