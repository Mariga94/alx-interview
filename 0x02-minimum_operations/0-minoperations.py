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
    minimumOp = 0
    m = 2
    while m > 1:
      while n % m:
        m += 1
      minimumOp += m
      n = int(n / m)
    return minimumOp 

