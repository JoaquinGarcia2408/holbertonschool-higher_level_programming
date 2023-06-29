#!/usr/bin/python3
"task 0"
from models.base import Base


class Rectangle(Base):

    "class Rectangle that inherits from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        "Validate attributes"
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be > 0")
        if y < 0:
            raise ValueError("y must be > 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        "Width getter"
        return self.__width

    @width.setter
    def width(self, value):
        "width setter"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "x getter"
        return self.__x

    @x.setter
    def x(self, value):
        "x setter"
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        "y getter"
        return self.__y

    @y.setter
    def y(self, value):
        "y setter"
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        "public method, returns the area value "
        return (self.__height * self.__width)

    def display(self):
        "that prints in stdout the Rectangle"
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        "overriding the __str__ method"
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
            f" - {self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        "Assigns an argument to each attribute"
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        "returns the dictionary representation of a Rectangle"
        return (
            {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
            }
        )
