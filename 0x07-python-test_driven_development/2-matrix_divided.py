#!/usr/bin/python3
"""matrix divided module"""


def matrix_divided(matrix, div):
    """Returns: new matrix"""
	
    matrix_lists_len = -1
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(matrix_error)
    for list_of_int in matrix:
	
        if not isinstance(list_of_int, list):
            raise TypeError(matrix_error)

        if not all(isinstance(num, (int, float)) for num in list_of_int):
            raise TypeError(matrix_error)
			
        if matrix_lists_len == -1:
            matrix_lists_len = len(list_of_int)
        elif matrix_lists_len != len(list_of_int):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for list_of_int in matrix:
        my_row = []
        for number in list_of_int:
            my_row.append(round(number / div, 2))
        new_matrix.append(my_row)
    return new_matrix
