#!/usr/bin/python3
"task 0"
from models.base import Base


class Rectangle(Base):

    "class Rectangle that inherits from Base"
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self, value):
        "Width getter"
        return self.__width

    @width.setter
    def width(self, value):
        "width setter"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "height getter"
        return self.__height

    @height.setter
    def height(self, value):
        "height setter"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be > 0")
        self.height = value

    @property
    def x(self):
        "x getter"
        return self.__x

    @x.setter
    def x(self, value):
        "x setter"
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise TypeError("x must be > 0")
        self.__x = value

    @property
    def yx(self):
        "y getter"
        return self.__y

    @x.setter
    def y(self, value):
        "y setter"
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise TypeError("y must be > 0")
        self.__y = value