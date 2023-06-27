#!/usr/bin/python3
"task 3"
import json


def to_json_string(mi_obj):
    """
    function that returns the JSON representation of an object (string)

    dumps: This function receives two parameters:

    the object with the data to be serialized, 

    and the file where the data will be written.
    """
    return json.dumps(mi_obj)
