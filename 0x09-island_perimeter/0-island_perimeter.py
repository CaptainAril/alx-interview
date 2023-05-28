#!/usr/bin/python3
"""Checks the perimeter of an island.
"""


def island_perimeter(grid):
    """Returns the parameter of an island (grid)"""
    row = len(grid)
    if row == 0:
        return
    column = len(grid[0])
    perimeter = 0

    for i in range(row):
        for j in range(column):

            if grid[i][j] == 1:
                # check left

                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1

                # check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # check right
                if j == column - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

                # check bottom
                if i == row - 1 or grid[i + 1][j] == 0:

                    perimeter += 1
    return perimeter
