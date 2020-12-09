while True:
    N = input()
    if N == '0':
        break
    i = 11
    tarSum = sum([int(c) for c in N])
    Nint = int(N)
    while True:
        if sum([int(c) for c in str(Nint * i)]) == tarSum:
            print(i)
            break
        i += 1