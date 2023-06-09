#!/usr/bin/python3
"Task 5 of more_classes"


class Rectangle():
    "Defines a rectangle (based on 0-rectangle.py)"
    def __init__(self, width=0, height=0):
        "Instantiation"
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        "Getter of the width"
        return self.__width

    @property
    def height(self):
        "Getter of the height"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter of the height"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        "Setter of the width"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        "Returns the rectangle area"
        return self.__height * self.__width

    def perimeter(self):
        "Returns the rectangle perimeter"
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        "String representation of the rectangle"
        if self.__height == 0 or self.__width == 0:
            return ""
        nString = ""
        for i in range(self.__height):
            for j in range(self.__width):
                nString += "#"
            if i < (self.__height) - 1:
                nString += "\n"
        return nString

    def __repr__(self):
        "Representation of the rectangle"
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        print("Bye rectangle...")
