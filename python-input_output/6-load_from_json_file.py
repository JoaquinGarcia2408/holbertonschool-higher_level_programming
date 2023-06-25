#!/usr/bin/python3
"task 6"
import json


def cargar_desde_archivo_json(nombre_archivo):
    "creates an Object from a “JSON file”"
    with open(nombre_archivo, 'r') as archivo:
        obj = json.load(archivo)
    return obj
