while True:
    W, L = [int(ea) for ea in input().split(' ')]
    if W == 0 and L == 0:
        break
    N = int(input())
    ax, ay, tx, ty = [0]*4
    for n in range(N):
        line = input().split(' ')
        dist = int(line[1])
        if line[0] == 'u':
            ay = min(L - 1, ay + dist)
            ty += dist
        elif line[0] == 'd':
            ay = max(0, ay - dist)
            ty -= dist
        elif line[0] == 'r':
            ax = min(W - 1, ax + dist)
            tx += dist
        else:  # line[0] == 'l'
            ax = max(0, ax - dist)
            tx -= dist
    print('Robot thinks', tx, ty)
    print('Actually at', ax, ay)
    print('')