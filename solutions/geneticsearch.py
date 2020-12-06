while True:
    line = input()
    if line == '0':
        break
    S, L = line.split(' ')
    type1 = {S}
    type2 = {S[:i] + S[i+1:] for i in range(len(S))}
    type3 = {S[:i] + 'A' + S[i:] for i in range(len(S)+1)}
    type3 = type3.union({S[:i] + 'G' + S[i:] for i in range(len(S)+1)})
    type3 = type3.union({S[:i] + 'C' + S[i:] for i in range(len(S)+1)})
    type3 = type3.union({S[:i] + 'T' + S[i:] for i in range(len(S)+1)})

    i = 0
    j1 = i + len(S)
    j2 = i + len(S) - 1
    j3 = i + len(S) + 1

    t1Count = 0
    t2Count = 0
    t3Count = 0

    while i < len(L):
        if L[i:j1] in type1:
            t1Count += 1
        if L[i:j2] in type2:
            t2Count += 1
        if L[i:j3] in type3:
            t3Count += 1
        i += 1
        j1 += 1
        j2 += 1
        j3 += 1

    print(t1Count, t2Count, t3Count)