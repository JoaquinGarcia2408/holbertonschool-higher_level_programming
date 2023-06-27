#!/usr/bin/python3
"Task 0"


def append_write(filename="", text=""):
    "appends a string text file (UTF8) and returns the number of characters added"
    with open(filename, mode='a', encoding='utf-8') as archivo:
        archivo.write(text)
    return (len(text))
