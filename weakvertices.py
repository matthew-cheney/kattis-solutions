def getNeighbors(targ, matrix, excl=None):
    if excl is None:
        excl = set()
    return {my_x for my_x in range(len(matrix[targ])) if matrix[targ][my_x] == '1' and my_x not in excl}

while True:
    N = int(input())
    if N == -1:
        break
    matr = []
    for n in range(N):
        matr.append(input().split(' '))
    weak_verts = set()
    for i in range(N):
        neighbors = getNeighbors(i, matr)
        tri_found = False
        for neighbor in neighbors:
            n_neighbors = getNeighbors(neighbor, matr, {i})
            if len(neighbors.intersection(n_neighbors)) > 0:
                tri_found = True
        if not tri_found:
            weak_verts.add(i)
    print(*sorted(list(weak_verts)))