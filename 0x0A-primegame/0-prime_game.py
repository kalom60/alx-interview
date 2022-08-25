#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """match between Maria and Ben"""
    Ben, Maria = 0, 0
    for i in range(x):
        ben, maria = 0, 0
        if (nums[i] == 1):
            ben += 1
        else:
            for num in range(nums[i] + 1):
                if num > 1:
                    for i in range(2, num):
                        if (num % i == 0):
                            break
                    else:
                        if ben == maria:
                            maria += 1
                        elif ben < maria:
                            ben += 1
        if (maria < ben):
            Ben += 1
        elif (ben < maria):
            Maria += 1
        else:
            Ben += 1
    if Ben < Maria:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
