import sys

lines = sys.stdin.readlines()

for line in lines:
    if line.strip() == '':
        continue
    a, b = [int(x) for x in line.split(' ')]
    print(abs(a - b))