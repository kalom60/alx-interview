#!/usr/bin/python3

from typing import List


def minOperations(n: int) -> int:
    cp: int = 0
    h: List[int] = [x for x in range(1, n) if n % x == 0]
    hcls: List[int] = [max(h)]
    while True:
        if hcls[-1] != 1:
            hcl: int = max(x for x in range(1, hcls[-1]) if hcls[-1] % x == 0)
            hcls.append(hcl)
        else:
            break

    for x in range(1, len(h) + 1):
        if x in hcls:
            cp += 2
        else:
            cp += 1

    return cp
