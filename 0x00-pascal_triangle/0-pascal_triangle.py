#!/usr/bin/python3
"""python module for pascal triangle"""


def factorial(n):
    """Calculate factorial of a number"""
    if n in [0, 1]:
        return 1
    if n == 2:
        return 2
    return n * factorial(n - 1)



