N = int(input())

points = []
for n in range(N):
    t, v = [float(ea) for ea in input().split(' ')]
    points.append((t, v))

total = 0
for i in range(N - 1):
    total += (points[i][1] + points[i+1][1]) * (points[i+1][0] - points[i][0]) / 2000

print(total)