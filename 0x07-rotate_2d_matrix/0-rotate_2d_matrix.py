#!/usr/bin/python3
"""
Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """Rotate a 2d matrix 90 degrees clockwise
    Arguments
        matrix (array): nested array
    Returns: nothing
    """
    lst = []
    for num in zip(*matrix):
        lst.append(list(reversed([*num])))
    matrix[:] = lst
