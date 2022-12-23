#!/usr/bin/python3
"""
Lists of integers representing the Pascal's triangle
of n
"""


def pascal_triangle(n):
    """
    """
    lst = []
    if n <= 0:
        return []
    for i in range(n):
        lst.append(map(str, str(11**i)))
    return lst
