import sys

lines = sys.stdin.readlines()

VOWELS = set('aeiouy')

for line in lines:
    line = line.strip()
    translatedLine = []
    for w in line.split(' '):
        if w[0] in VOWELS:
            translatedLine.append(w + 'yay')
        else:
            cons = ''
            for c in w:
                if c in VOWELS:
                    break
                cons += c
            translatedLine.append(w[len(cons):] + cons + 'ay')
    print(*translatedLine)