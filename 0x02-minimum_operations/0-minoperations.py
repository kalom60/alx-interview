#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    return the min operation that takes to write h n times
    """

    cp = last = 0
    h = 'H'
    while len(h) < n:
        if n % len(h) == 0:
            last = len(h)
            h = h * 2
            cp += 2
        else:
            h += last * 'H'
            cp += 1

    return cp
