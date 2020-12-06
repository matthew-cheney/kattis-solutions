from queue import Queue

def main():
    N, M = [int(x) for x in input().split(' ')]

    grid = []
    for n in range(N):
        grid.append([int(x) for x in list(input())])

    # Each edge is same weight - BFS

    distances = dict()
    for n in range(N):
        for m in range(M):
            distances[(n, m)] = 0

    q = Queue()
    q.put((0, 0))
    visited = set()
    visited.add((0,0))
    while q.qsize() > 0:
        cur = q.get()
        if cur[0] == N-1 and cur[1] == M-1:
            print(distances[cur])
            return

        dist = grid[cur[0]][cur[1]]
        neighbors = list()
        neighbors.append((cur[0] + dist, cur[1]))
        neighbors.append((cur[0] - dist, cur[1]))
        neighbors.append((cur[0], cur[1] + dist))
        neighbors.append((cur[0], cur[1] - dist))

        for neighbor in [x for x in neighbors if x[0] < N and x[0] >= 0 and x[1] < M and x[1] >= 0]:
            if neighbor in visited:
                continue
            q.put(neighbor)
            distances[neighbor] = distances[cur] + 1
            visited.add(neighbor)
    print(-1)



main()