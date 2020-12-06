from queue import Queue

X, Y = [int(ea) for ea in input().split(' ')]

matr = []

for y in range(Y):
    matr.append([int(ea) for ea in input().split(' ')])

validArea = 0
unvisited = {(i, j) for i in range(Y) for j in range(X)}

while len(unvisited) > 0:
    cur = unvisited.pop()
    unvisited.add(cur)
    q = Queue()
    q.put(cur)
    visited = set()
    valid = True
    level = matr[cur[0]][cur[1]]
    levelSize = 0
    while q.qsize() > 0:
        cur = q.get()
        if cur in visited:
            continue
        visited.add(cur)
        unvisited.remove(cur)
        levelSize += 1
        if cur[0] > 0:
            if matr[cur[0]-1][cur[1]] == level and (cur[0]-1, cur[1]) not in visited:
                q.put((cur[0]-1, cur[1]))
            elif matr[cur[0]-1][cur[1]] < level:
                valid = False
        if cur[0] < Y - 1:
            if matr[cur[0]+1][cur[1]] == level and (cur[0]+1, cur[1]) not in visited:
                q.put((cur[0]+1, cur[1]))
            elif matr[cur[0]+1][cur[1]] < level:
                valid = False
        if cur[1] > 0:
            if matr[cur[0]][cur[1]-1] == level and (cur[0], cur[1]-1) not in visited:
                q.put((cur[0], cur[1]-1))
            elif matr[cur[0]][cur[1]-1] < level:
                valid = False
        if cur[1] < X - 1:
            if matr[cur[0]][cur[1]+1] == level and (cur[0], cur[1]+1) not in visited:
                q.put((cur[0], cur[1]+1))
            elif matr[cur[0]][cur[1]+1] < level:
                valid = False
    validArea += levelSize * valid
print(validArea)