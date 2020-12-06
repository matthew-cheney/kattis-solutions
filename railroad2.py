x, y = [int(ea) for ea in input().split(' ')]
if ((4 * x) + (3 * y)) % 2 == 0:
    print('possible')
else:
    print('impossible')