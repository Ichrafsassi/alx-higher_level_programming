#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for coll in row:
            print("{:d}".format(coll), end=" " if coll != row[-1] else "")
        print()
