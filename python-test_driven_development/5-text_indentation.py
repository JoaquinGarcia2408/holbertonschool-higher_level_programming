#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = " "
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            result += text[i] + "\n\n"
        else:
            result += text[i]
    print(result.strip())
