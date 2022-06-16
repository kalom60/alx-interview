#!/usr/bin/python3
"""python module for pascal triangle"""


def pascal_triangle(n):
    """evaluate and return pascal triangle"""

    if n == 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal[i].append(1)
    return pascal
