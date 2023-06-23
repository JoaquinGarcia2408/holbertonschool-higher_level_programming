#!/usr/bin/python3
"Task 0"


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as archivo:
        archivo.write(text)
    return (len(text))
