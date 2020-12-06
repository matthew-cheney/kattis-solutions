T = int(input())

for t in range(T):
    imp = 0
    turts = [int(ea) for ea in input().split(' ')]
    for i in range(1, len(turts) - 1):
        if turts[i] > turts[i-1] * 2:
            imp += turts[i] - (turts[i-1] * 2)
    print(imp)