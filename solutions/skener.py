R, C, Zr, Zc = [int(ea) for ea in input().split(' ')]

for r in range(R):
    row = input()
    newRow = ''
    for c in row:
        for z in range(Zc):
            newRow += c
    for z in range(Zr):
        print(newRow)