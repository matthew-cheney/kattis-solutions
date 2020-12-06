from collections import deque

M, N = [int(x) for x in input().split(' ')]

matr = []

for m in range(M):
    matr.append(list(input()))

unvisited = set()

for m in range(M):
    for n in range(N):
        if matr[m][n] == '#':
            unvisited.add((m, n))

loops = 0
while len(unvisited) > 0:
    loops += 1
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
        q.append((r,c-1))
        q.append((r-1,c))
        q.append((r,c+1))
        q.append((r+1,c))
        q.append((r-1,c-1))
        q.append((r+1,c+1))
        q.append((r+1,c-1))
        q.append((r-1,c+1))

print(loops)