T = int(input().strip())

for t in range(T):
    line = input().strip().split(' ')
    N, K = int(line[0]), int(line[1])

    snaps = 0

    for i in range(K):
        cur = snaps
        bit = 0
        while bit < N and cur & 1 == 1:
            snaps ^= 2 ** bit
            bit += 1
            cur >>= 1
        if bit < N:
            snaps ^= 2 ** bit
            bit += 1

    if snaps == (2 ** N) - 1:
        print(f'Case #{t+1}: ON')
    else:
        print(f'Case #{t+1}: OFF')
