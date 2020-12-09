class UFDS:

    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes)]
        self.rank = [0 for i in range(num_nodes)]

    def __repr__(self):
        return f'parents: {self.parent}\n' \
               f'ranks: {self.rank}'

    def findSet(self, n):
        if self.parent[n] == n:
            return n
        p = self.findSet(self.parent[n])
        self.parent[n] = p
        self.rank[n] = self.rank[p] + 1
        return p

    def isSameSet(self, n, m):
        return self.findSet(n) == self.findSet(m)

    def union(self, n, m):
        if not self.isSameSet(n, m):
            n_set = self.findSet(n)
            m_set = self.findSet(m)
            if self.rank[n_set] > self.rank[m_set]:
                self.parent[m_set] = n_set
            else:
                self.parent[n_set] = m_set
                self.rank[m_set] += 1 if self.rank[n_set] == self.rank[m_set] else 0


R, C = [int(ea) for ea in input().split(' ')]
matr = []
for r in range(R):
    matr.append(list(input()))

def getNumRep(coord):
    return (coord[0] * C) + coord[1]

U = UFDS(1 + R * C)

for r in range(R):
    for c in range(C):
        if r > 0 and matr[r][c] == matr[r - 1][c]:
            U.union(getNumRep((r, c)), getNumRep((r - 1, c)))
        if r < R - 1 and matr[r][c] == matr[r + 1][c]:
            U.union(getNumRep((r, c)), getNumRep((r + 1, c)))
        if c > 0 and matr[r][c] == matr[r][c - 1]:
            U.union(getNumRep((r, c)), getNumRep((r, c - 1)))
        if c < C - 1 and matr[r][c] == matr[r][c + 1]:
            U.union(getNumRep((r, c)), getNumRep((r, c + 1)))

N = int(input())

for n in range(N):
    r1, c1, r2, c2 = [int(ea) - 1 for ea in input().split(' ')]
    if U.isSameSet(getNumRep((r1, c1)), getNumRep((r2, c2))):
        print('binary' if matr[r1][c1] == '0' else 'decimal')
    else:
        print('neither')