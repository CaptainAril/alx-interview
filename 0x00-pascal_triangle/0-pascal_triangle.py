#!/usr/bin/python3
"""returns a list of lists of integers representing the Pascal's
triangle of `n`.
"""


def pascal_triangle(n):
    """Return's pascal's triangle.

    Args:
        n (int): size of the pascal's triangle

    Returns:
        list: list of lists of integers representing pascal's triangle.
    """
    if n <= 0:
        return []

    pascal_list = []
    for i in range(n):
        temp_list = []

        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                num = pascal_list[i-1][j-1] + pascal_list[i-1][j]
                temp_list.append(num)
        pascal_list.append(temp_list)
    return pascal_list
