while True:
    N = int(input().strip())
    if N == 0:
        break
    reg = [False for i in range(32)]
    cert = [False for i in range(32)]
    for n in range(N):
        line = input().strip().split(' ')
        if line[0] == 'SET':
            i = int(line[1])
            reg[i] = True
            cert[i] = True
        elif line[0] == 'CLEAR':
            i = int(line[1])
            reg[i] = False
            cert[i] = True
        elif line[0] == 'AND':
            i, j = int(line[1]), int(line[2])
            if cert[i] and not reg[i]:
                continue
            if cert[j] and not reg[j]:
                reg[i] = False
                cert[i] = True
                continue
            if cert[i] and cert[j]:
                reg[i] = reg[i] and reg[j]
            else:
                cert[i] = False
        else: # == 'OR'
            i, j = int(line[1]), int(line[2])
            if cert[i] and reg[i]:
                continue
            if cert[j] and reg[j]:
                reg[i] = True
                cert[i] = True
                continue
            if cert[i] and cert[j]:
                reg[i] = reg[i] or reg[j]
            else:
                cert[i] = False

    for i in range(31, -1, -1):
        if cert[i]:
            print(int(reg[i]), end='')
        else:
            print('?', end='')
    print('')