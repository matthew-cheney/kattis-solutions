from queue import Queue


def getNeighbors(coord, board):
    r = coord[0]
    c = coord[1]
    neighbors = list()
    N = len(board)
    neighbors.append((r + 2, c + 1))
    neighbors.append((r + 2, c - 1))
    neighbors.append((r - 2, c + 1))
    neighbors.append((r - 2, c - 1))
    neighbors.append((r + 1, c + 2))
    neighbors.append((r + 1, c - 2))
    neighbors.append((r - 1, c + 2))
    neighbors.append((r - 1, c - 2))
    return [x for x in neighbors if x[0] < N and x[0] >= 0 and x[1] < N and x[1] >= 0]

def main():
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(input()))

    # find K
    K_coord = (0,0,0)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'K':
                K_coord = (i, j, 0)

    if K_coord == (0, 0, 0):
        print(0)
        return

    # Because all edges are same weight, we use a BFS

    visited = set()
    q = Queue()
    q.put(K_coord)
    while q.qsize() > 0:
        cur = q.get()
        if cur[:2] in visited:
            continue
        visited.add(cur[:2])
        if board[cur[0]][cur[1]] == '#':
            continue
        if cur[0] == 0 and cur[1] == 0:
            print(cur[2])
            return
        for neighbor in getNeighbors(cur, board):
            q.put((neighbor[0], neighbor[1], cur[2] + 1))
    print(-1)


main()
