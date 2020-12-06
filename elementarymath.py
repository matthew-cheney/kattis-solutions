N = int(input())

G = [[] for n in range(N)]

problemKey = [[]]*N
answerKey = [tuple()]*N
revAnswerKey = dict()

nodeKey = [0]*N

ans_i = N
for n in range(N):
    l, r = [int(ea) for ea in input().split(' ')]

    nodeKey[n] = [l, r]

    if l + r not in revAnswerKey:
        revAnswerKey[l + r] = ans_i
        nodeKey.append(l + r)
        ans_i += 1
    if l - r not in revAnswerKey:
        revAnswerKey[l - r] = ans_i
        nodeKey.append(l - r)
        ans_i += 1
    if l * r not in revAnswerKey:
        revAnswerKey[l * r] = ans_i
        nodeKey.append(l * r)
        ans_i += 1

    G[n].append(revAnswerKey[l + r])
    G[n].append(revAnswerKey[l - r])
    G[n].append(revAnswerKey[l * r])

# problems on left
# answers on right

matched = [-1]*len(nodeKey)
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

if MCBM < N:
    print('impossible')
    exit(0)

for i, ans in enumerate(matched[N:]):
    if ans > -1:
        nodeKey[ans].append(nodeKey[N + i])

for l, r, ans in nodeKey[:N]:

    if l + r == ans:
        print(l, '+', r, '= ', ans)
    elif l - r == ans:
        print(l, '-', r, '= ', ans)
    else:
        print(l, '*', r, '= ', ans)
