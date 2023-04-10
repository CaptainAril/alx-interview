#!/usr/bin/python3
"""Minimum Operations."""

import math


def minOperations(n):
    """Returns the fewest number of operations needed to
    multiply a single character (copy and paste operations)
    to `n` number of characters."""
    if n == 1:
        return 0

    number_of_operations = 0
    char = 2
    while (char <= n):
        if (n % char == 0):
            n = int(n / char)
            number_of_operations += char
            char = 1
        char += 1
    return number_of_operations
