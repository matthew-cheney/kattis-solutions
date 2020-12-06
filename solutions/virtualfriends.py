class UFDS:

    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes+1)]
        # self.rank = [0 for i in range(num_nodes+1)]
        self.children = [[i] for i in range(num_nodes+1)]
        self.in_find = list()

    def __repr__(self):
        return f'parents: {self.parent}\n'
               # f'ranks: {self.rank}'

    def groupSize(self, n):
        return len(self.children[self.findSet(n)])

    def findSet(self, n):
        cur = n
        while self.parent[cur] != cur:
            cur = self.parent[cur]
        return cur

    def isSameSet(self, n, m):
        return self.findSet(n) == self.findSet(m)

    def union(self, n, m):
        if not self.isSameSet(n, m):
            n_set = self.findSet(n)
            m_set = self.findSet(m)
            # if self.rank[n_set] > self.rank[m_set]:
            if len(self.children[n_set]) > len(self.children[m_set]):
                self.parent[m_set] = n_set
                for child in self.children[m_set]:
                    self.children[n_set].append(child)
            else:
                self.parent[n_set] = m_set
                # self.rank[m_set] += 1 if self.rank[n_set] == self.rank[m_set] else 0
                for child in self.children[n_set]:
                    self.children[m_set].append(child)

T = int(input())

for t in range(T):
    F = int(input())
    friendships = list()
    people = set()
    for f in range(F):
        line = input().split(' ')
        people.add(line[0])
        people.add(line[1])
        friendships.append(line)
    d = {v: i for i, v in enumerate(people)}
    U = UFDS(len(people))
    for frnd in friendships:
        U.union(d[frnd[0]], d[frnd[1]])
        print(U.groupSize(d[frnd[0]]))
