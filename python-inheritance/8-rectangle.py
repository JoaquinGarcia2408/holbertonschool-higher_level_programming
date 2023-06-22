#!/usr/bin/python3
"task 8"


class BaseGeometry:
    "based on 5-base_geometry.py"
    def area(self):
        "Public instance method"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    "class Rectangle that inherits from BaseGeometry"
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
