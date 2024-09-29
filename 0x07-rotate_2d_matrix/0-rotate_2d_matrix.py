#!/usr/bin/python3
"""a module to rotate an n x x 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """rotate a 2D matrix 90 degrees clockwise in-place"""
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = (
                matrix[i][n - 1 - j], matrix[i][j])
