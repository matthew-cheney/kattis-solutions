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

N, K = [int(x) for x in input().split(' ')]

U = UFDS(N)

for k in range(K):
    a, b = [int(x) for x in input().split(' ')]
    U.union(a,b)

good = True
i = 1
while good and i <= N // 2:
    good = U.isSameSet(i, N - (i - 1))
    i += 1

print(('Yes' if good else 'No'))
