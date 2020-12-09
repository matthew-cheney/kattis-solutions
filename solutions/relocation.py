N, Q = [int(ea) for ea in input().split(' ')]
locs = [0] + [int(ea) for ea in input().split(' ')]

for q in range(Q):
    C, arg1, arg2 = [int(ea) for ea in input().split(' ')]
    if C == 1:
        locs[arg1] = arg2
    else:
        print(abs(locs[arg1] - locs[arg2]))