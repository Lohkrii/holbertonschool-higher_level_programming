#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(0, len(matrix)):
        for cidx in range(0, len(matrix[idx])):
            print("{:d}".format(matrix[idx][cidx]), end="")
            if (cidx < len(matrix[idx]) - 1):
                print(" ", end="")
        print("\n", end="")
