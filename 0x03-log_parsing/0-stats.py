#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys


if __name__ == "__main__":
    status_code = {"200": 0,
                   "301": 0,
                   "400": 0,
                   "401": 0,
                   "403": 0,
                   "404": 0,
                   "405": 0,
                   "500": 0
                   }
    on_ten = 0
    file_size = 0

    def parse_line(line):
        """ parse a line"""
        parsed_line = line.split(' ')
        code = parsed_line[-2]
        if code in status_code:
            status_code[code] += 1
        return int(parsed_line[-1])

    def print_stats():
        """display the stat"""
        print(f'File size: {file_size}')
        for k, v in status_code.items():
            if v:
                print(f'{k}: {v}')

    try:
        for line in sys.stdin:
            file_size += parse_line(line)
            on_ten += 1
            if on_ten == 10:
                print_stats()
                on_ten = 0
    except KeyboardInterrupt:
        print_stats()
        sys.exit(1)
