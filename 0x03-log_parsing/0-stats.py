#!/usr/bin/python3
"""
this module is manly for the log parsing project in
ALX
"""

import sys
import re

def print_statistics(total_size, status_codes):
    """Prints statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """Parses a single line of log data"""
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return int(match.group(3)), int(match.group(2))
    return None, None

def main():
    """Main function"""
    total_size = 0
    status_codes = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                total_size += file_size
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass #keyboard interupt

    print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
