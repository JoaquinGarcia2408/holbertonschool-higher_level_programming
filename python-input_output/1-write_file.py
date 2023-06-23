#!/usr/bin/python3
"Task 0"


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as archivo:
        caracteres_escritos = archivo.write(text)
    return caracteres_escritos
