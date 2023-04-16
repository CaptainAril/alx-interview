#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""


def returnLog(total_size, statsCode):
    """Prints statistics."""
    print("File size: {}".format(total_size))
    for key, value in sorted(statsCode.items()):
        print("{}: {}".format(key, value))


def log():
    """Reads stdin line by line and computes metrics."""
    import sys
    count = 0
    total_size = 0
    statsCode = {}
    possible_code = [200, 301, 400, 401, 403, 404, 405, 500]
    try:
        for line in sys.stdin:
            count += 1
            splt = line.split(' ')
            try:
                code = int(splt[7])
                size = int(splt[8])
                total_size += size
                if code not in possible_code:
                    continue
                if code in statsCode.keys():
                    statsCode[code] += 1
                else:
                    statsCode[code] = 1

            except Exception:
                pass

            if count == 10:
                returnLog(total_size, statsCode)
                count = 0
        returnLog(total_size, statsCode)

    except KeyboardInterrupt:
        returnLog(total_size, statsCode)
        raise


if __name__ == '__main__':
    log()
