#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total > 0:
        amount = [total + 1 for _ in range(total + 1)]
        amount[0] = 0
        for a in range(1, total + 1):
            for c in coins:
                if a - c >= 0:
                    amount[a] = min(amount[a], 1 + amount[a - c])
        if amount[total] != total + 1:
            return amount[total]
        return -1
    return 0
