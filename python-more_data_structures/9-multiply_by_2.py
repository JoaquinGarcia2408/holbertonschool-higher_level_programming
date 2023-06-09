#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        print("Dictionary is None")
        return
    dup = a_dictionary
    for i in dup:
        dup[i] *= 2
    return dup