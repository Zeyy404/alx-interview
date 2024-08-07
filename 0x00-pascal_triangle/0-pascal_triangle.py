#!/usr/bin/python3
"""
a function that returns a list of lists of
integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Pascal Triangle logic"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        new_row = [1]

        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            new_row.append(value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
