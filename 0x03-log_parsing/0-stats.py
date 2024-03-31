#!/usr/bin/python3
"""
this module is manly for the log parsing project in
ALX
"""

import sys


def print_statistics(total_size, status_codes):
    """ Prints status """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def parse_line(line):
    """ Parses lines (return) """
    parts = line.split()
    if len(parts) >= 7 and parts[5].isdigit():
        return int(parts[5]), int(parts[6])
    return None


def main():
    """ the main is the start of the program(entry)"""
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            data = parse_line(line)
            if data:
                file_size, status_code = data
                total_size += file_size
                status_codes[status_code] = \
                    status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass #handle keybARD INTERUPTION

    print_statistics(total_size, status_codes)


if __name__ == "__main__":
    main()
