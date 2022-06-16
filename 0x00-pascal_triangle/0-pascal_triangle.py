#!/usr/bin/python3
"""python module for pascal triangle"""


def pascal_triangle(n):
    """evaluate and return pascal triangle"""

    def factorial(val):
        """Calculate factorial of a number"""
        if val in [0, 1]:
            return 1
        if val == 2:
            return 2
        return val * factorial(val - 1)

    if n <= 0:
        return []
    pascal = [[int(factorial(num) / (factorial(num - num1) * factorial(num1)))
               for num1 in range(num+1)] for num in range(n)]

    return pascal
