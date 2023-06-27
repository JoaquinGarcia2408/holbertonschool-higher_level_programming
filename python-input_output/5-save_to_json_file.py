#!/usr/bin/python3
"task 5"
import json


def save_to_json_file(mi_obj, nombre_archivo):
    "function that writes an Object to a text file"
    with open(nombre_archivo, 'w') as archivo:
        json.dump(mi_obj, archivo)
