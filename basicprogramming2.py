N, t = [int(ea) for ea in input().split(' ')]
A = [int(ea) for ea in input().split(' ')]

if t == 1:
    setA = set(A)
    found = False
    for x in A:
        if 7777 - x in setA:
            found = True
            break
    print('Yes' if found else 'No')
elif t == 2:
    print('Unique' if len(A) == len(set(A)) else "Contains duplicate")
elif t == 3:
    counts = dict()
    for x in A:
        if x not in counts:
            counts[x] = 0
        counts[x] += 1
    found = False
    val = 0
    for x in A:
        if counts[x] > N // 2:
            val = x
            found = True
    print(val if found else -1)
elif t == 4:
    A.sort()
    if len(A) % 2 == 0:
        print(A[(len(A) // 2) - 1], A[len(A) // 2])
    else:
        print(A[len(A) // 2])
else:  # t == 5
    A.sort()
    nums = []
    for x in A:
        if x >= 100 and x <= 999:
            nums.append(x)
    print(*nums)