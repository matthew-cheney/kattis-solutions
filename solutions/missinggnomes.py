N, M = [int(ea) for ea in input().split(' ')]
missing = set(range(1, N + 1))
present = list()
for m in range(M):
    g = int(input())
    missing.remove(g)
    present.append(g)

missing = sorted(list(missing))

mi, pi = 0, 0
while mi < len(missing) and pi < len(present):
    if missing[mi] < present[pi]:
        print(missing[mi])
        mi += 1
    else:
        print(present[pi])
        pi += 1

while mi < len(missing):
    print(missing[mi])
    mi += 1

while pi < len(present):
    print(present[pi])
    pi += 1
