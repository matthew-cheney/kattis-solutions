N = int(input())
for n in range(N):
    line = [int(ea) for ea in input().split(' ')]
    print(sum(line[1:]) + 1 - line[0])