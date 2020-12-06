import sys
from collections import deque

lines = sys.stdin.readlines()

inputI = 0
case = 0

while inputI < len(lines):
    case += 1
    line = lines[inputI].strip()
    inputI += 1
    M, N = [int(x) for x in line.split(' ')]
    matr = []
    for m in range(M):
        matr.append(list(lines[inputI].strip()))
        inputI += 1
    unvisited = set()
    for m in range(M):
        for n in range(N):
            if matr[m][n] == '-':
                unvisited.add((m, n))
    stars = 0
    while len(unvisited) > 0:
        stars += 1
        cur = unvisited.pop()
        unvisited.add(cur)
        q = deque()
        q.append(cur)
        while len(q) > 0:
            cur = q.pop()
            if cur not in unvisited:
                continue
            unvisited.remove(cur)
            r, c = cur
            q.append((r, c-1))
            q.append((r, c+1))
            q.append((r-1, c))
            q.append((r+1, c))
    print(f'Case {case}: {stars}')