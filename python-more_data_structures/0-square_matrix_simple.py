#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for row in matrix:
        new_row = []
        for elemento in row:
            new_row.append(elemento ** 2)
        copy_matrix.append(new_row)
    return copy_matrix
