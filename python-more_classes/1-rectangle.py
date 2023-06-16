#!/usr/bin/python3
"Task 0 of more_classes"


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        # Asignar los valores proporcionados a los atributos _width y _height
        self.__width = width
        self.__height = height

        # Validaciones para width y height (estas validaciones se pueden mover a los setters si se prefiere)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        "definir una propiedad llamada width"
        return self._width

    @width.setter
    def width(self, value):
        "Setter width"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        "definir una propiedad llamada height"
        return self._height

    @height.setter
    def height(self, value):
        "Setter height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
