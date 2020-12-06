N, S, T = [int(each) for each in input().split(' ')]

matr = list()
for n in range(N):
    matr.append([int(each) for each in input().split(' ')])

pq = set()

BIG = 1000000

visited = set()


class Node:
    def __init__(self, val, dist):
        self.val = val
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

    def __repr__(self):
        return f'{self.val}: {self.dist}'


nodes = {each: Node(each, matr[S][each]) for each in range(N)}
unvisited = {node for node in nodes.values()}

for node in nodes.values():
    if node.val == S:
        continue
    pq.add(node)

while len(pq) > 0:
    # get cur
    cur = Node(-1, 100000000)
    for each in pq:
        if each.dist < cur.dist:
            cur = each
    pq.remove(cur)
    visited.add(cur)
    unvisited.remove(cur)
    for each in unvisited:
        each.dist = min(each.dist, cur.dist + matr[cur.val][each.val])

print(nodes[T].dist)
