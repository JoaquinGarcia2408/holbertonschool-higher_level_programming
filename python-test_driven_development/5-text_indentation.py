#!/usr/bin/python3
"Task 4"


def text_indentation(text):
    '''Prints a text with 2 new lines after each of
    these characters: ".", "?" and ":"'''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space_check = False
    for i in range(len(text)):
        if text[i] in {".", "?", ":"}:
            print()
            print()
            space_check = True
        if space_check:
            if i < len(text) - 1 and text[i + 1] == " ":
                continue
            space_check = False
        else:
            print(text[i], end="")
