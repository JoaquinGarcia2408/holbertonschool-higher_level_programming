#!/usr/bin/python3
"Task 10"
from models.rectangle import Rectangle


class Square(Rectangle):
    "class Square that inherits from Rectangle"
    def __init__(self, size, x=0, y=0, id=None):
        "Class constructor"
        super().__init__(size, size, x, y, id)
