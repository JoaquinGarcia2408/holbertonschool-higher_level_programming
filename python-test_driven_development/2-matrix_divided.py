#!/usr/bin/python3
def matrix_divided(matrix, div):
    err = "matrix must be a matrix (list of lists) of integers/floats"
    divmatrix = []
    lon = len(matrix[0])
    for row in matrix:
        if len(row) != lon:
            raise TypeError("Each row of the matrix must have the same size")
        for eche in row:
            if not isinstance(eche, (int, float)):
                raise TypeError(err)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        divrow = []
        for eche in row:
            divelemnt = round(eche / div, 2)
            divrow.append(divelemnt)
        divmatrix.append(divrow)
    return divmatrix
