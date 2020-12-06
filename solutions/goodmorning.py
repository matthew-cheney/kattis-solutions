from collections import deque

T = int(input())

neighbors = {'': {1,2,3,4,5,6,7,8,9},
             '1': {1,2,3,4,5,6,7,8,9,0},
             '2': {2,3,5,6,8,9,0},
             '3': {3,6,9},
             '4': {4,5,6,7,8,9,0},
             '5': {5,6,8,9,0},
             '6': {6,9},
             '7': {7,8,9,0},
             '8': {8,9,0},
             '9': {9},
             '0': {0}}

for t in range(T):
    k = int(input())
    q = deque()
    for n in neighbors['']:
        q.append(str(n))
    visited = set()
    closest = 400
    while len(q) > 0:
        cur = q.pop()
        if cur in visited:
            continue
        visited.add(cur)
        if int(cur) == k:
            closest = int(cur)
            break
        if abs(k - int(cur)) > (2 * k) + 1:
            continue
        if abs(k - int(cur)) < abs(k - closest):
            closest = int(cur)
        for n in neighbors[cur[-1]]:
            q.append(cur + str(n))
    print(closest)