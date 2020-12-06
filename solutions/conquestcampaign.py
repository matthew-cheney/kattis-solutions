from queue import Queue

R, C, N = [int(x) for x in input().split(' ')]

q = Queue()

for n in range(N):
    x, y = [int(each) for each in input().split(' ')]
    q.put((x-1,y-1, 0))

visited = set()

deepest = 0
while q.qsize() > 0:
    cur = q.get()
    depth = cur[2]
    if cur[:2] in visited:
        continue
    deepest = max(deepest, depth)
    visited.add(cur[:2])
    if cur[0] > 0:
        q.put((cur[0]-1, cur[1], depth+1))
    if cur[0] < R - 1:
        q.put((cur[0]+1, cur[1], depth+1))
    if cur[1] > 0:
        q.put((cur[0], cur[1]-1, depth+1))
    if cur[1] < C - 1:
        q.put((cur[0], cur[1]+1, depth+1))

print(deepest + 1)