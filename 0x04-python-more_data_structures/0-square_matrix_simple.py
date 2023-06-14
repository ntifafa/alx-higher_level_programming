#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    output = [[0] * len(row) for row in matrix]

    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            output[row][element] = matrix[row][element] ** 2
    return output
