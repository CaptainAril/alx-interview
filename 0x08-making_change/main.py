#!/usr/bin/python3
""" Main file for testing
"""

makechange = __import__('0-making_change').makeChange

print(makechange([1, 2, 25], 37))

print(makechange([1256, 54, 48, 16, 102], 1453))
