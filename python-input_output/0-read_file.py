#!/usr/bin/python3
"Task 0"


def read_file(filename=""):
    "function that reads a text file (UTF8) and prints it to stdout"
    with open(filename, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido, end="")
