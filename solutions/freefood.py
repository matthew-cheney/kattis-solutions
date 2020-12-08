N = int(input())

days = [0]*366
for n in range(N):
    s, e = [int(ea) for ea in input().split(' ')]
    for i in range(s, e + 1):
        days[i] = 1
print(sum(days))