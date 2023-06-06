#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return
    for fila in range(len(matrix)):
        for columna in range(len(matrix[fila])):
            print("{:d}".format(matrix[fila][columna]), end="")
            if columna < len(matrix[fila]) - 1:
                print(end=" ")
        print()
