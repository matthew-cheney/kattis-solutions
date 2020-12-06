N, K = [int(x) for x in input().split(' ')]

watches = set()

for k in range(K):
    watches.add(int(input()) - 1)

total = N * (N - 1)
total //= 2

streak = False
dangInARow = 0
for h in range(N):
    if h not in watches:
        # dangerous house
        # continuing dangerous streak
        if streak:
            dangInARow += 1
        # starting dangerous streak
        else:
            streak = True
            dangInARow += 1
    else:
        # ending dangerous streak
        if streak:
            dangWalks = dangInARow * (dangInARow - 1)
            dangWalks //= 2
            total -= dangWalks
            streak = False
            dangInARow = 0
        # all safe
        # do nothing

# check last streak
if streak:
    dangWalks = dangInARow * (dangInARow - 1)
    dangWalks //= 2
    total -= dangWalks

# add walks to own house
total += len(watches)

print(total)