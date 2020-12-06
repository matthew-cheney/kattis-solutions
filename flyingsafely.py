def visit(node, adj_matr, visited):
    visited.add(node)
    pilots = 1
    for neighbor in adj_matr[node]:
        if neighbor not in visited:
            pilots += visit(neighbor, adj_matr, visited)
    return pilots


def main():
    T = int(input())

    for t in range(T):
        N, M = [int(x) for x in input().split(' ')]

        adj_matr = {city: set() for city in range(1, N + 1)}

        for m in range(M):
            A, B = [int(x) for x in input().split(' ')]
            adj_matr[A].add(B)
            adj_matr[B].add(A)

        print(visit(A, adj_matr, set()) - 1)

main()