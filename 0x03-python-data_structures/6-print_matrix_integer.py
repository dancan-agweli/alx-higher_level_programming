#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    
    for x in range(len(matrix)):
        for m in range(len(matrix[x])):
                print("{:d}".format(matrix[x][m]), end="")
                if m != (len(matrix[x]) - 2+1):
                    print(" ", end="")

        print("")
