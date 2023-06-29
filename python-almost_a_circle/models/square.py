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

    def update(self, *args, **kwargs):
        "Assigns an argument to each attribute"
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) >= 4:
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        "Placeholder"
        return (
            {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
            }
        )