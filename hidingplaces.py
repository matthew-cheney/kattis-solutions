from queue import Queue

N = int(input())

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def __repr__(self):
        return self.name

nodes = {}

for c in '12345678':
    for d in '12345678':
        nodes[c + d] = Node(chr(int(c) + 96) + d)

# build chess board
for row in range(1, 9):
    for col in range(1, 9):
        src = str(row) + str(col)
        if row > 1:
            if col > 2:
                nodes[src].neighbors.append(nodes[str(row - 1) + str(col - 2)])
            if col < 7:
                nodes[src].neighbors.append(nodes[str(row - 1) + str(col + 2)])
        if row < 8:
            if col > 2:
                nodes[src].neighbors.append(nodes[str(row + 1) + str(col - 2)])
            if col < 7:
                nodes[src].neighbors.append(nodes[str(row + 1) + str(col + 2)])
        if col > 1:
            if row > 2:
                nodes[src].neighbors.append(nodes[str(row - 2) + str(col - 1)])
            if row < 7:
                nodes[src].neighbors.append(nodes[str(row + 2) + str(col - 1)])
        if col < 8:
            if row > 2:
                nodes[src].neighbors.append(nodes[str(row - 2) + str(col + 1)])
            if row < 7:
                nodes[src].neighbors.append(nodes[str(row + 2) + str(col + 1)])

keys_to_ints = {k: i for i, k in enumerate(nodes.keys())}
ints_to_keys = {i: k for i, k in enumerate(nodes.keys())}

NUM_NODES = len(nodes)
BIG = 100000

for n in range(N):
    pos = input()
    pos = str(ord(pos[0]) - 96) + pos[1]
    # do BFS from pos
    visited = set()
    visit_next = Queue()
    visit_next.put((nodes[pos], 0))
    furthest_nodes = []
    furthest_dist = 0
    while visit_next.qsize() > 0:
        curTup = visit_next.get()
        cur = curTup[0]
        dist = curTup[1]
        if cur in visited:
            continue
        visited.add(cur)
        if dist == furthest_dist:
            furthest_nodes.append(cur)
        elif dist > furthest_dist:
            furthest_dist = dist
            furthest_nodes = [cur]
        for child in cur.neighbors:
            visit_next.put((child, dist + 1))
    print(furthest_dist, end=' ')
    print(*sorted(furthest_nodes, key=lambda x: (10 - int(x.name[1]), x.name[0])))