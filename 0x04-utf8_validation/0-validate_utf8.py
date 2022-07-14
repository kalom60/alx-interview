#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    return True if data is valid UTF-8 encoding
    else return False
    """
    num = 0
    for i in data:
        if num == 0:
            if (i >> 5) == 0b110:
                num = 1
            elif (i >> 4) == 0b1110:
                num = 2
            elif (i >> 3) == 0b11110:
                num = 3
            elif (i >> 7):
                return False
        else:
            if (i >> 6) != 0b10:
                return False
            num -= 1
    return True
