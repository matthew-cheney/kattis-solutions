P = int(input())
for i in range(P):
    line = input().split(' ')
    K = int(line[0])
    N = int(line[1])
    odd_sum = 0
    even_sum = 0
    for j in range(1, N + 1):
        if j % 2 == 0:
            even_sum += j
        else:
            odd_sum += j
    pos_sum = even_sum + odd_sum
    for j in range(N + 1, (2 * N) + 1):
        if j % 2 == 0:
            even_sum += j
        else:
            odd_sum += j
    print(K, pos_sum, odd_sum, even_sum)