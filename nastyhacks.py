n = int(input())
for i in range(n):
    line = input().split(' ')
    r, e, c = int(line[0]), int(line[1]), int(line[2])
    if r > e - c:
        print('do not advertise')
    elif e - c > r:
        print('advertise')
    else:
        print('does not matter')