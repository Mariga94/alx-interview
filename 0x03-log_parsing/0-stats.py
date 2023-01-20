#!/usr/bin/python3
"""Log Parsing Module"""
import sys

status_codes = {'200': 0, '301': 0, '400': 0,
                '401': 0, '403': 0, '404': 0,
                '405': 0, '500': 0}
total_size = 0


def print_stats():
    """Prints all current stats"""
    print("File size: {}".format(total_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k]:
            print("{}: {}".format(k,  status_codes[k]))


try:
    for i, line in enumerate(sys.stdin, start=1):
        matches = line.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
            total_size += int(file_size)
        except Exception:
            pass
        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
