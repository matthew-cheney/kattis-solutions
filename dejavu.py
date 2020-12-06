N = int(input())

byX = dict()
byY = dict()
points = list()
for n in range(N):
    x, y = input().split(' ')
    if x not in byX:
        byX[x] = list()
    if y not in byY:
        byY[y] = list()
    byX[x].append(y)
    byY[y].append(x)
    points.append((x, y))

total = 0
for xp, yp in points:
    total += (len(byX[xp]) - 1) * (len(byY[yp]) - 1)

print(total)