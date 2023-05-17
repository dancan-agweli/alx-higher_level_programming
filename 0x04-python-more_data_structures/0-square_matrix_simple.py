#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    data = []

    if len(matrix) > 0:
        for u in matrix[:]:
            data.append(list(map(lambda x: x ** 2, u)))
    return data
