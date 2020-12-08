first = True

while True:
    N = int(input())
    if N == 0:
        break
    if first:
        first = False
    else:
        print('')
    l1 = []
    for n in range(N):
        l1.append(int(input()))
    l2 = []
    for n in range(N):
        l2.append(int(input()))
    l1Sorted = sorted(l1)
    l2.sort()
    mappings = dict()
    for i in range(N):
        mappings[l1Sorted[i]] = l2[i]
    for i in range(N):
        print(mappings[l1[i]])
