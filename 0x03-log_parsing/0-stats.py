#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import sys
import re
from collections import defaultdict


LOG_PATTERN = re.compile(
    r'^.* - \[.*\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    )

total_size = 0
status_counts = defaultdict(int)
line_count = 0


try:
    for line in sys.stdin:
        match = LOG_PATTERN.match(line)
        if match:
            status_code, file_size = match.groups()
            file_size = int(file_size)
            if status_code in {'200', '301', '400', '401',
                               '403', '404', '405', '500'}:
                status_counts[status_code] += 1

            total_size += file_size
            line_count += 1

        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code in sorted(status_counts):
                count = status_counts[code]
                if count > 0:
                    print(f"{code}: {count}")

except Exception as e:
    pass

finally:
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        count = status_counts[code]
        if count > 0:
            print(f"{code}: {count}")
