from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

import sys

lines = sys.stdin.readlines()
line_i = 0

while line_i < len(lines):

    N, M, S, V = [int(ea) for ea in lines[line_i].split(' ')]
    line_i += 1

    G = dict()
    gopher_coords = dict()
    node_i = 0
    for n in range(N):
        g = tuple([float(ea) for ea in lines[line_i].split(' ')])
        line_i += 1
        G[node_i] = list()
        gopher_coords[node_i] = g
        node_i += 1

    keys = tuple(G.keys())
    for n in range(N):
        hole = tuple([float(ea) for ea in lines[line_i].split(' ')])
        line_i += 1
        G[node_i] = list()
        for g in keys:
            if dist(*gopher_coords[g], *hole) / V <= S:
                G[g].append(node_i)
                G[node_i].append(g)
        node_i += 1

    # run MCBM algorithm
    matched = [-1]*node_i
    visited = [0]*len(G)

    def augmenting_path(left, visited, matched):
        if visited[left]:
            return 0
        visited[left] = True

        for right in G[left]:
            if matched[right] == -1 or augmenting_path(matched[right], visited, matched):
                matched[right] = left
                matched[left] = right
                return 1
        return 0

    MCBM = 0
    for left in range(N):
        visited = [0]*node_i
        MCBM += augmenting_path(left, visited, matched)

    print(N - MCBM)

