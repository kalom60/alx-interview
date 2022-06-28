#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    return the min operation that takes to write h n times
    """
    cp = 0
    h = [x for x in range(1, n) if n % x == 0]
    hcls = [max(h)]
    if hcls == 1:
        return 0

    while True:
        if hcls[-1] != 1:
            hcl = max(x for x in range(1, hcls[-1]) if hcls[-1] % x == 0)
            hcls.append(hcl)
        else:
            break

    for x in range(1, len(h) + 1):
        if x in hcls:
            cp += 2
        else:
            cp += 1

    return cp
