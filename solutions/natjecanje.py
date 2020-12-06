from collections import deque

N, S, R = [int(x) for x in input().split(' ')]
odamaged = {int(x)-1 for x in input().split(' ')}
oreserves = {int(x)-1 for x in input().split(' ')}

# remove teams that supply selves with reserve
damaged = [x for x in odamaged if x not in oreserves]
reserves = [x for x in oreserves if x not in odamaged]

startState = ['' for i in range(N)]
for d in damaged:
    startState[d] = 'D'
for r in reserves:
    startState[r] = 'L'

q = deque()
q.append(tuple(startState))
visited = set()
bssf = len(damaged)
while len(q) > 0:
    cur = q.pop()
    if cur in visited:
        continue
    visited.add(cur)
    newBssf = 0
    for i in range(1, len(cur) - 1):
        if cur[i] == 'D' and cur[i-1] != 'R' and cur[i+1] != 'L':
            newBssf += 1
    if cur[0] == 'D' and cur[1] != 'L':
        newBssf += 1
    if cur[-1] == 'D' and cur[-2] != 'R':
        newBssf += 1
    bssf = min(bssf, newBssf)
    for r in reserves:
        newState = list(cur)
        newState[r] = 'R' if newState[r] == 'L' else 'L'
        q.append(tuple(newState))
print(bssf)