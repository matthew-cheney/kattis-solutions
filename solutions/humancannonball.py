# start is a node
# end is a node
# each cannon is a node

# dist start to cannon: beeline to cannon
# dist start to end: beeline to end
# dist cannon to cannon: launch to closest point then beeline
# dist cannon to end: min(beeline to end, launch to closest point then beeline)

# run at 5 m/s
# cannon shoots 25 m/s
from math import sqrt

CRANGE = 50

CTIME = 2  # time to launch in cannon

RPACE = 5
CPACE = 25

BIG = float('INF')

def closestPointOnRadius(cx, cy, dx, dy):
    x_delta = dx - cx
    y_delta = dy - cy
    dist_to_d = sqrt(x_delta ** 2 + y_delta ** 2)
    ratio = CRANGE / dist_to_d
    return cx + (x_delta * ratio), cy + (y_delta * ratio)

def getNext(unvisited, dist):
    return sorted(unvisited, key=lambda x: dist[x])[0]

def getRunTime(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / RPACE

def getCannonTime(cx, cy, dx, dy):
    run_time = getRunTime(cx, cy, dx, dy)
    cannon_time = CTIME + getRunTime(*closestPointOnRadius(cx, cy, dx, dy), dx, dy)
    return min(run_time, cannon_time)


def main():
    sx, sy = [float(x) for x in input().split(' ')]
    ex, ey = [float(x) for x in input().split(' ')]
    N = int(input())

    if N == 0:
        return getRunTime(sx, sy, ex, ey)

    # read in cannons
    unvisited = set()
    dist = dict()  # actually stores time, not distance
    for n in range(N):
        cannon = tuple([float(x) for x in input().split(' ')])
        unvisited.add(cannon)
        dist[cannon] = getRunTime(sx, sy, cannon[0], cannon[1])

    visited = set()
    while len(unvisited) > 0:
        cur = getNext(unvisited, dist)
        unvisited.remove(cur)
        visited.add(cur)
        for c in unvisited:
            dist[c] = min(dist[c], dist[cur] + getCannonTime(cur[0], cur[1], c[0], c[1]))

    # include run time from start to end directly
    dist_to_end = min([dist[c] + getCannonTime(c[0], c[1], ex, ey) for c in visited] + [getRunTime(sx, sy, ex, ey)])
    return dist_to_end


print(main())