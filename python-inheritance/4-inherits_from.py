#!/usr/bin/python3
"task 4"


def inherits_from(obj, a_class):
    "returns True if the object is an instance of a class that inherited"

    return (isinstance(obj, a_class) and type(obj) != a_class)
