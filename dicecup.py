from collections import Counter

N, M = [int(ea) for ea in input().split(' ')]

sums = []

for n in range(1, N+1):
    for m in range(1, M+1):
        sums.append(n + m)

C = Counter(sums)
sortedC = sorted(C.items(), key=lambda x: x[1], reverse=True)

mostProb = sortedC[0][1]

for k, v in sortedC:
    if v == mostProb:
        print(k)