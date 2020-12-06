from queue import PriorityQueue

N, K = [int(x) for x in input().split(' ')]

visited = set()
dist = dict()

BIG = 1000000

class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        if value == 1:
            self.distance = 0
        else:
            self.distance = BIG

nodes_by_value = dict()
seen_vals = [False for k in range(K)]

for n in range(N):
    line = [int(each) for each in input().split(' ')]
    for i, v in enumerate(line):
        if v not in nodes_by_value:
            nodes_by_value[v] = set()
        nodes_by_value[v].add(Node(i, n, v))
        seen_vals[v-1] = True

# check if no paths exist
if not all(seen_vals):
    print(-1)
    exit(0)

for i in range(2, K+1):
    # look at each row in layer
    for each in nodes_by_value[i]:
        # look at each node in previous layer
        for prev in nodes_by_value[i-1]:
            each.distance = min(each.distance, prev.distance + abs(each.x - prev.x) + abs(each.y - prev.y))

# get min distance in final layer
ans = min([each.distance for each in nodes_by_value[K]])
print(ans)