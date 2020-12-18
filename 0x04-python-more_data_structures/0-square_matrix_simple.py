#!/usr/bin/python3
def square_nums(num):
    return num * num


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for num in matrix:
        new_matrix.append(list(map(square_nums, num)))
    return new_matrix
