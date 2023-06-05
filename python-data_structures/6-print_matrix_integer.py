def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for num in fila:
            print("{:d}".format(num), end=" ")
        print()