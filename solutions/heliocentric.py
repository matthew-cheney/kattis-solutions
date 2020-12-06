EARTH = 365
MARS = 687

import sys

lines = sys.stdin.readlines()

for i, line in enumerate(lines):
    if line == '':
        continue
    e, m = [int(ea) for ea in line.split(' ')]
    days = 0
    while e != m:
        e += 1
        e %= EARTH
        m += 1
        m %= MARS
        days += 1
    print(f'Case {i+1}: {days}')