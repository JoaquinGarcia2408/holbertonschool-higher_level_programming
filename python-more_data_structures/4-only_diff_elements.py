#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    for i in set_1:
        for j in set_2:
            if (i == j):
                elements = i
    set_2.remove(elements)
    set_1.remove(elements)
    set_3 = set_1 | set_2
    return set_3
