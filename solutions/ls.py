P = input()
N = int(input())

BIG = 10001

for n in range(N):
    f = input()
    matr = [[BIG for i in range(len(f) + 1)] for j in range(len(P) + 1)]
    matr[0][0] = 0
    i = 0
    while i < len(P) and P[i] == '*':
        matr[i+1][0] = 0
        i += 1
    for row in range(1, len(matr)):
        for col in range(1, len(matr[0])):
            if P[row - 1] == '*':
                matr[row][col] = min(matr[row-1][col], matr[row][col-1], matr[row-1][col-1])
            elif P[row - 1] == f[col - 1]:
                matr[row][col] = matr[row-1][col-1]
    if matr[-1][-1] == 0:
        print(f)
