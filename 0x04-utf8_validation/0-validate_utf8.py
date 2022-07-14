#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    return True if data is valid UTF-8 encoding
    else return False
    """
    count = 0
    if len(data) == 0:
        return True

    for c in data:
        bit = 1 << 7
        if count != 0:
            if not (c & 1 << 7 and not (c & 1 << 6)):
                return False
        else:
            while (bit & c):
                count += 1
                bit = bit >> 1

            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
        count -= 1

    if count == 0:
        return True
    return False
