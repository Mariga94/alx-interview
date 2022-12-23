#!/usr/bin/python3
"""
Program that returns a lists a lists of integers representing the
Pascal's triangle of n
"""


def pascal_triangle(n):
    """Defines the pascal function
    Args
      n (int): n lines
    Returns: a list of n lines else, return empty list
    """
    lst = []
    if n <= 0:
        return []
    for i in range(n):
        lst.append(map(str, str(11**i)))
    return lst
