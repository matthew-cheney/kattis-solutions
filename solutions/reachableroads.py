from queue import Queue

N = int(input())


for n in range(N):
    M = int(input())
    neighbors = {str(i): set() for i in range(M+1)}
    R = int(input())
    for r in range(R):
        f, s = input().split(' ')
        neighbors[f].add(s)
        neighbors[s].add(f)
    unvisited = {str(i) for i in range(M)}
    roadsNeeded = 0
    while len(unvisited) > 0:
        roadsNeeded += 1
        cur = unvisited.pop()
        unvisited.add(cur)
        visited = set()
        q = Queue()
        q.put(cur)
        while q.qsize() > 0:
            cur = q.get()
            if cur in visited:
                continue
            visited.add(cur)
            unvisited.remove(cur)
            for nghb in neighbors[cur]:
                q.put(nghb)
    print(roadsNeeded - 1)