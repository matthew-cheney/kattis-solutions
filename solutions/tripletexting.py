msg = input()
dist = len(msg) // 3

p0, p1, p2 = 0, dist, 2 * dist

def maj(a0, a1, a2):
    if a0 == a1 or a0 == a2:
        return a0
    else:
        return a1

for i in range(dist):
    print(maj(msg[p0], msg[p1], msg[p2]), end='')
    p0 += 1
    p1 += 1
    p2 += 1
print('')