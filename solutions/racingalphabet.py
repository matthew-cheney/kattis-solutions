from math import pi

N = int(input())

locs = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ \'')

unit = (60 * pi) / 28

for n in range(N):
    line = list(input())
    cur = locs.index(line[0])
    dist = 0
    for i in range(len(line) - 1):
        between = abs(locs.index(line[i]) - locs.index(line[i+1]))
        dist += unit * min(between, 28 - between)
    print(len(line) + dist / 15)