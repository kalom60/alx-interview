#!/usr/bin/python3
"""python module for pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    value = [[str(11 ** num)] for num in range(n)]
    val = [num2 for num in value for num2 in num]
    return val
