N = int(input())

for n in range(N):
    a, b, c = [int(ea) for ea in input().split(' ')]
    if c in [a + b, a - b, b - a, a * b, a / b, b / a]:
        print('Possible')
    else:
        print('Impossible')