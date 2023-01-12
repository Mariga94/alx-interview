#!/usr/bin/python3
"""
0-minoperations module
"""


def minOperations(n):
    """Calculates the fewest number of operations needed
    to result in exactly n H characters in the file

    Args:
      n (int): number of H

    Return:
        minimum number of operations
    """
    minO = 0
    m = 2
    while isinstance(n, int) and n > 1:
        while n % m:
            m += 1
        minO += m
        n = int(n / m)
    return minO
