line = input().split(' ')
H = int(line[0])
H += 1
path = line[1]
numNodes = 0
for i in range(H):
    numNodes += 2 ** i

if len(path) == 0:
    print(numNodes)
    exit(0)

k = 0
for move in path:
    k *= 2
    k += 1 + (move == 'R')

print(numNodes - k)