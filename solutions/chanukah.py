P = int(input())

for p in range(P):
    I, N = [int(ea) for ea in input().split(' ')]
    print(I, sum(range(N+1)) + N)