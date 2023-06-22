#!/usr/bin/python3
"task 10"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        "subclass square"
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        "return area"
        return self.__size ** 2

    def __str__(self):
        "printer"
        return f"[Rectangle] {self.__size}/{self.__size}"
