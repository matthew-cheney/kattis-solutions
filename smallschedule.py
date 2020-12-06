Q, M, S, L = [int(x) for x in input().split(' ')]

totalTime = 0

# fill as many complete layers with Q as possible
filledWithQ = L // M
totalTime += filledWithQ * Q
L = L % M

# put remaining Qs on next layer, fit in 1s on remaining machines
if L > 0:
    totalTime += Q
    machinesNotUsedByQs = M - L
    S -= machinesNotUsedByQs * Q

# fill as many complete layers with 1s as possible
if S > 0:
    filledWithS = S // M
    totalTime += filledWithS
    S = S % M

    # if 1s remain, they fill less than 1 layer
    if S > 0:
        totalTime += 1

print(totalTime)
