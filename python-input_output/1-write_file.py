#!/usr/bin/python3
"Task 0"


def write_file(filename="", text=""):
    "writes a string to a text file (UTF8) and returns the number of characters written"
    with open(filename, "w", encoding="utf-8") as archivo:
        caracteres_escritos = archivo.write(text)
    return caracteres_escritos
