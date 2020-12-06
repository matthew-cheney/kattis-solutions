N, M = [int(ea) for ea in input().split(' ')]

G = [[] for i in range(M + N)]
for m in range(M):
    person, book = [int(ea) for ea in input().split(' ')]
    G[person].append(N + book)

matched = [-1]*(2*N)
visited = [0]*N

def augmenting_path(left):
    global visited
    if visited[left]:
        return 0
    visited[left] = True

    for right in G[left]:
        if matched[right] == -1 or augmenting_path(matched[right]):
            matched[right] = left
            matched[left] = right
            return 1
    return 0

MCBM = 0
for left in range(N):
    visited = [0]*N
    MCBM += augmenting_path(left)

if MCBM == N:
    print('YES')
else:
    print('NO')