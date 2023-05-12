#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Takes a nxn matrix and rotates it 90 clockwise in place


    Args:
        matrix (_type_): n x n matrix. Assume matrix will not be empty
    """
    lgth = len(matrix)
    for x in range(lgth):
        for y in range(x, lgth):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    for row in matrix:
        row.reverse()
