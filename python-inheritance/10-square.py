#!/usr/bin/python3
"Task 10"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "A subclass square of the base class rectangle"
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        "Returns the area"
        return self.__size ** 2

    def __str__(self):
        "Printer"
        return f"[Rectangle] {self.__size}/{self.__size}"
