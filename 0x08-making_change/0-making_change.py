#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total > 0:
        count = 0
        coins = sorted(coins)
        coins.reverse()
        for coin in coins:
            while(total >= coin):
                count += 1
                total -= coin
        if total != 0:
            return -1
        return count
    return 0
