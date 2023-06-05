#!/usr/bin/python3
def no_c(my_string):
    space = ""
    for i in my_string:
        if i == "c" or i == "C":
            continue
        else:
            space += i
    return space
