#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """Define a square object"""
    def __init__(self, size=0):
        """Initializes a new instance of square class with
         a given size

         Args:
         size (int): The size of the square."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Initialize a new instance"""
        return self.__size ** 2