N = int(input())

cups = []
for n in range(N):
    line = input().split(' ')
    if 48 <= ord(line[0][0]) <= 57:
        num = int(line[0]) // 2
        col = line[1]
    else:
        num = int(line[1])
        col = line[0]
    cups.append((num, col))
cups.sort()
for c in cups:
    print(c[1])