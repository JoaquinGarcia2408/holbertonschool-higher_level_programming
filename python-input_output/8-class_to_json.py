#!/usr/bin/python3
"Task 8"


def class_to_json(obj):
    """Returns the dic description with simple
    data structure, for JSON serialization of an object

    Args:
        obj : An instance of a class
    """
    return obj.__dict__
