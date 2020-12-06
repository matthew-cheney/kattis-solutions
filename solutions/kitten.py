K = input()

class Node:
    def __init__(self, val):
        self.val = val
        self.children = set()
        self.parents = set()


node_dict = {}

while True:
    line = input()
    if line == '-1':
        break
    line = line.split(' ')
    n = line[0]
    if n not in node_dict:
        node_dict[n] = Node(n)
    for c in line[1:]:
        if c not in node_dict:
            node_dict[c] = Node(c)
        node_dict[n].children.add(node_dict[c])
        node_dict[c].parents.add(node_dict[n])

def dfs(node, target):
    if node.val == target:
        return [node.val]
    for c in node.children:
        path = dfs(c, target)
        if path != []:
            return path + [node.val]
    return []

# Find root
root = ''
for n in node_dict.values():
    if len(n.parents) == 0:
        root = n
        break

print(*[int(each) for each in dfs(root, K)])