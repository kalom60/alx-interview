#!/usr/bin/python3
"""LockBoxes"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""
    outerSize = 0
    keys = []
    for outer in boxes:
        if len(outer) > 0:
            outerSize += 1
            for inner in outer:
                keys.append(inner)

    keys = set(keys)
    if outerSize == len(keys):
        return True
    else:
        return False
