#!/usr/bin/python3
"Task 10"
from models.rectangle import Rectangle


class Square(Rectangle):
    "class Square that inherits from Rectangle"
    def __init__(self, size, x=0, y=0, id=None):
        "Class constructor"
        super().__init__(size, size, x, y, id)

    @property
    def size(self, value):
        "Width getter"
        return self.width

    @size.setter
    def size(self, value):
        "size setter"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
