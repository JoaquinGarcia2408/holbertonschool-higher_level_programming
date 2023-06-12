#!/usr/bin/python3
"""clase Cuadrado que define un cuadrado"""
class Square:
    """La clase Square define un objeto cuadrado."""
    def __init__(self, size=0):
        """Inicializa una nueva instancia de la clase Square con un tamaño dado """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """se inicializa una nueva instacia pubica"""
    def area(self):
        return self.__size ** 2