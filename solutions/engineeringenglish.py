import sys

lines = sys.stdin.readlines()

seen = set()
for line in lines:
    out = []
    for word in line.split(' '):
        lowered = word.lower().strip()
        if lowered not in seen:
            seen.add(lowered)
            out.append(word.strip())
        else:
            out.append('.')
    print(*out)