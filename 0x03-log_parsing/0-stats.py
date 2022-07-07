#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys
from signal import signal, SIGINT


status_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}
file_size = 0
on_ten = 0


def display_metrics():
    """display the metrics"""
    print(f'File size: {file_size}')
    for k, v in status_code.items():
        if v:
            print(f'{k}: {v}')


def handler(sig, frame):
    """CTRL + C handler"""
    display_metrics()
    sys.exit(1)


signal(SIGINT, handler)

for lines in sys.stdin:
    line = lines.split(' ')
    minus = line[1]
    method = line[4][1:]
    http = line[6].split('/')[0]
    code = line[7]
    size = line[-1].split('\\')[0]
    if minus == '-' and code in status_code and \
            http == 'HTTP' and method == 'GET':
        if on_ten == 10:
            display_metrics()
            on_ten = 0

        status_code[code] += 1
        file_size += int(size)
        on_ten += 1
