#!/usr/bin/python3
"""This module defines a lockbox function.
"""


def canUnlockAll(boxes):
    """Function that receives a list of boxes,
    and detarmines if all the boxes can be opened."""
    n = len(boxes)
    box_stat = []
    for i in range(n):
        box_stat.append(False)
    keys = boxes[0]
    box_stat[0] = True

    for i in range(1, n):
        temp_key = []
        for key in keys:
            if key < n and box_stat[key] is False:
                temp_key.extend(boxes[key])
                box_stat[key] = True
        keys = temp_key

    return False if False in box_stat else True
