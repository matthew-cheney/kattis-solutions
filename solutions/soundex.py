import sys

lines = sys.stdin.readlines()

letterToInt = {
    '$': 0,
    'B': 1,
    'F': 1,
    'P': 1,
    'V': 1,
    'C': 2,
    'G': 2,
    'J': 2,
    'K': 2,
    'Q': 2,
    'S': 2,
    'X': 2,
    'Z': 2,
    'D': 3,
    'T': 3,
    'L': 4,
    'M': 5,
    'N': 5,
    'R': 6
}

for line in lines:
    if line == '':
        continue
    prevChar = '$'
    for c in line:
        if c in letterToInt and (prevChar not in letterToInt or letterToInt[c] != letterToInt[prevChar]):
            print(letterToInt[c], end='')
        prevChar = c
    print('')
