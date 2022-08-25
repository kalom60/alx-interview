#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """match b/n Maria and Ben"""
    if x < 1 or not nums:
        return None
    Ben, Maria = 0, 0

    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        Ben += primes_count % 2 == 0
        Maria += primes_count % 2 == 1
    if Ben == Maria:
        return None
    if Ben < Maria:
        return 'Maria'
    else:
        return 'Ben'
