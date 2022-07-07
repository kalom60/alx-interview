#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""


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

checker = {
    'method': '"GET /projects/260 HTTP/1.1"',
}

file_size = 0
on_ten = 0


def check_ip(ip):
    """validate ip address"""
    ip = ip.split('.')
    if len(ip) == 4:
        for addy in ip:
            if addy.isdigit() and \
                    (int(addy) < 0 and int(addy) > 255):
                return True
            return False
    return False


def display_metrics():
    """display the metrics"""
    print(f'File size: {file_size}')
    for k, v in status_code.items():
        if v:
            print(f'{k}: {v}')


try:
    for lines in input():
        line = lines.split(' ')
        ip = line[0]
        dates = line[2][1:] + line[3][:-1]
        dates = datetime.strptime(dates, "%Y-%m-%d%H:%M:%S.%f")
        minus = line[1]
        method = line[4] + ' ' + line[5] + ' ' + line[6]
        code = line[7]
        size = line[-1].split('\\')[0]
        if minus == '-' and code in status_code and \
                method == checker['method'] and check_ip(ip) \
                    and isinstance(dates, datetime):
            if on_ten == 10:
                display_metrics()
                on_ten = 0
            status_code[code] += 1
            file_size += int(size)
            on_ten += 1
except KeyboardInterrupt:
    display_metrics()
else:
    display_metrics()
