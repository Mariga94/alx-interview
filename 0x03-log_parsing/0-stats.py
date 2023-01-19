#!/usr/bin/python3
"""Log Parsing Module"""
import sys

possible_status_codes = {200: 0, 301: 0, 400: 0,
                         401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0


def parse_line(line):
    """Parses line from file"""

    try:
        char = line.rstrip().split(' ')
        total_size += char[-1]

        if char[-2] in possible_status_codes:
            possible_status_codes[char[-2]] += 1
    except Exception:
        pass


def print_stats():
    """Prints all current stats"""
    print("File size: {}".format(total_size))
    for k in sorted(possible_status_codes.keys()):
        if possible_status_codes[k]:
            print("{}: {}".format(k,  possible_status_codes[k]))

n = 1

try:
    for line in sys.stdin:
        parse_line(line)
        if n % 10 == 0:
            print_stats()
            n += 1
except KeyboardInterrupt:
    print_stats()
    raise
print_stats()