#!/usr/bin/python3
"""LockBoxes"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""
    box_size = len(boxes)
    unlocked = [0]

    [unlocked.append(key) for keys in unlocked
        for key in boxes[keys]
        if key not in unlocked and key < box_size]

    return len(unlocked) == box_size
