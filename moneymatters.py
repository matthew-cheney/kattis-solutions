from queue import Queue

N, M = [int(x) for x in input().split(' ')]

balances = [0]*N
for n in range(N):
    balances[n] = int(input())

friends = {str(i): set() for i in range(N)}

for m in range(M):
    f1, f2 = input().split(' ')
    friends[f1].add(f2)
    friends[f2].add(f1)

unvisited = {str(i) for i in range(N)}
message = 'POSSIBLE'
while len(unvisited) > 0:
    cur = unvisited.pop()
    unvisited.add(cur)
    totalBalance = 0
    q = Queue()
    q.put(cur)
    visited = set()
    while q.qsize() > 0:
        cur = q.get()
        if cur in visited:
            continue
        visited.add(cur)
        unvisited.remove(cur)
        totalBalance += balances[int(cur)]
        for frnd in friends[cur]:
            q.put(frnd)
    if totalBalance != 0:
        message = 'IMPOSSIBLE'
        break
print(message)