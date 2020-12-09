N = int(input())
if N == 1:
    input()
    print(1)
    exit(0)
pos = [int(ea) for ea in input().split(' ')]
line = [0]*(N - 1)
for i in range(N - 1):
    line[pos[i]] = i + 2
line = [1] + line
print(*line)