#!/usr/bin/python3
"task 10"
Rectangle = __import__('9-rectangle').Rectangle

class Square(rectangle):

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
    
    def area(self):
        return self.__size ** 2

    def __str__(self):
         return f"[Rectangle] {self.__width}/{self.__height}"
