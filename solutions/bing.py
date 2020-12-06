N = int(input())

class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.word = False
        self.prefixTo = 0

root = Node('$')

for n in range(N):
    word = input()
    cur = root
    for c in word:
        if c not in cur.children:
            cur.children[c] = Node(c)
        cur = cur.children[c]
        cur.prefixTo += 1
    cur.word = True
    print(cur.prefixTo - 1)