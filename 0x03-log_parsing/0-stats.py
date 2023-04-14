#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

count = 0
total_size = 0
statsCode = {}
possible_code = [200, 301, 400, 401, 403, 404, 405, 500]

for line in sys.stdin:
    if count == 10:
        for key, value in sorted(statsCode.items()):
            print("{}: {}".format(key, value))
        print("File size: {}".format(total_size))
        count = 0
        statsCode = {}

    try:
        count += 1
        splt = line.split(' ')
        try:
            size = int(splt[7])
            total_size += size
            code = int(splt[8])
            if code not in possible_code:
                continue
            statsCode[code] = count
            print("{}: {}".format(code, count))

        except Exception:
            pass

    except KeyboardInterrupt:
        sys.exit(0)
