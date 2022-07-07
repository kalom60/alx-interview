#!/usr/bin/python3
""""""
import sys
import re
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
line = None
check = None
on_ten = 0


def ip(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)"\
        r"{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if (re.search(pattern, ip)):
        return True
    return False


def minus(sign):
    if sign == '-':
        return True
    return False


def date(date):
    date = date[1:]
    matched = re.match(r'\d\d\d\d-\d\d-\d\d', date)
    if matched:
        return True
    return False


def time(time):
    matched = re.match(r'\d\d:\d\d:\d\d', time)
    if matched:
        return True
    return False


def method(method):
    method = method[1:]
    if method == 'GET':
        return True
    return False


def file(path):
    if path == '/projects/260':
        return True
    return False


def http(http):
    http = http[:-1]
    if http == 'HTTP/1.1':
        return True
    return False


def code(code):
    if code in status_code:
        return True
    return False


def size(size):
    if int(size) > 0:
        return True
    return False


def line_check():
    print(f'File size: {file_size}')
    for k, v in status_code.items():
        if v:
            print(f'{k}: {v}')


def handler(sig, frame):
    line_check()
    sys.exit(1)


file_format = {
    ip: None,
    minus: None,
    date: None,
    time: None,
    method: None,
    file: None,
    http: None,
    code: None,
    size: None
}

signal(SIGINT, handler)

for lines in sys.stdin:
    line = lines.split(' ')
    for c, k in enumerate(file_format.keys()):
        file_format[k] = line[c]

    val = []
    for k, v in file_format.items():
        val.append(k(v))
    check = val[:]

    if False not in check:
        if on_ten == 10:
            line_check()
            on_ten = 0

        status = file_format[code]
        status_code[status] += 1
        fsize = int(file_format[size])
        file_size += fsize
        on_ten += 1
