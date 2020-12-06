class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        self.leaf = False


T = int(input())

for t in range(T):
    N = int(input())
    trie = Node(None)
    valid = True
    for n in range(N):
        number = input()
        if number == '':
            continue
        if not valid:
            continue
        cur = trie
        for c in number:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
            # cur is a leaf, trying to walk over number = prefix
            if cur.leaf:
                valid = False
                break
        # finish the number, but still have children = prefix
        if len(cur.children) != 0:
            valid = False
        cur.leaf = True
    if valid:
        print('YES')
    else:
        print('NO')
