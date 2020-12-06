N, M = [int(ea) for ea in input().split(' ')]

G = [[] for m in range(M+1)]

studentI = M + 1
for n in range(N):
    line = input().split(' ')
    for slot in line[1:]:
        G[int(slot)].append(studentI)
    studentI += 1

# slots on the left
# students on the right

matched = [-1]*(N + M + 1)
visited = [0]*M

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
for left in range(M+1):
    visited = [0]*(M+1)
    MCBM += augmenting_path(left)

print(MCBM)