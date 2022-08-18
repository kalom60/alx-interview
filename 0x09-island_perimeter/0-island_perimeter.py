#!/usr/bin/python3
"""Island Perimeter module"""


def island_perimeter(grid):
    """return perimeter of island"""
    visited = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if ((j - 1) >= 0) or ((j + 1) <= len(grid[i])):
                    try:
                        if grid[i][j - 1] == 0:
                            visited += 1
                    except IndexError:
                        visited += 1
                    try:
                        if grid[i][j + 1] == 0:
                            visited += 1
                    except IndexError:
                        visited += 1
                if ((i - 1) >= 0) or ((i + 1) <= len(grid)):
                    try:
                        if grid[i - 1][j] == 0:
                            visited += 1
                    except IndexError:
                        visited += 1
                    try:
                        if grid[i + 1][j] == 0:
                            visited += 1
                    except IndexError:
                        visited += 1
    return visited
