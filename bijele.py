good = [1, 1, 2, 2, 2, 8]
line = [int(x) for x in input().split(' ')]
for i in range(len(good)):
    print(good[i] - line[i], end='')
    if i < len(good) - 1:
        print(' ', end='')
