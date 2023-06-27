#!/usr/bin/python3
"task 0"
from models.base import Base


class Rectangle(Base):

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