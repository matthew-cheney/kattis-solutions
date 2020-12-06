import sys

lines = sys.stdin.readlines()
for line in lines:
    if line == '':
        continue
    print('yes' if 'problem' in line.lower() else 'no')