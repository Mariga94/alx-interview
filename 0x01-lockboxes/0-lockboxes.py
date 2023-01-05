#!/usr/bin/python3
""" Determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """Function defination

    Args:
      boxes (list): List of list of boxes

    Returns:
      bool: True for success, False otherwise.
    """
    if not isinstance(boxes, list) or (len(boxes) == 0):
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box != 0 and key < len(boxes):
                keys.append(box)
    if len(boxes) == len(keys):
        return True
    return False
