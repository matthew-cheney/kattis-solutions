R, N = [int(ea) for ea in input().split(' ')]
rooms = [False]*R
for n in range(N):
    rooms[int(input()) - 1] = True
avail = -1
for r in range(R):
    if not rooms[r]:
        avail = r + 1
        break
print(avail if avail > -1 else "too late")