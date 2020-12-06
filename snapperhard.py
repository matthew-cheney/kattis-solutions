T = int(input().strip())

for t in range(T):
    line = input().strip().split(' ')
    N, K = int(line[0]), int(line[1])

    if (K + 1) % 2 ** N == 0:
        print(f'Case #{t + 1}: ON')
    else:
        print(f'Case #{t + 1}: OFF')
