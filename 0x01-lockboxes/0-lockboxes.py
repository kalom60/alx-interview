#!/usr/bin/python3
"""LockBoxes"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""
    unlocked = set()
    keys = [0]

    while keys:
        box = keys.pop()
        unlocked.add(box)
        [keys.append(key) for key in boxes[box]
            if key not in unlockeda nd key < len(boxes)]

    return len(boxes) == len(unlocked)
