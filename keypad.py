# for each cell
# if cell == 0, then there cannot be 1 in row and 1 in col
# if only 1 in row, then P
# if only 1 in col, then P
# if multiple 1s in row and in col, then I

T = int(input())

for t in range(T):
    R, C = [int(ea) for ea in input().split(' ')]
    matr = []
    ansMatr = [['N' for c in range(C)] for r in range(R)]
    for r in range(R):
        matr.append([int(ea) for ea in list(input())])
    valid = True
    for r in range(R):
        for c in range(C):
            rowSum = sum([x for x in matr[r]])
            colSum = sum([matr[x][c] for x in range(R)])
            if matr[r][c] == 0 and rowSum > 0 and colSum > 0:
                    valid = False
            if matr[r][c] == 1:
                if rowSum == 1 or colSum == 1:
                    ansMatr[r][c] = 'P'
                else:
                    ansMatr[r][c] = 'I'
    if not valid:
        print('impossible')
    else:
        for row in ansMatr:
            print(*row, sep='')
    print('----------')