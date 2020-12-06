l, r = [int(x) for x in input().split(' ')]
if l == 0 and r == 0:
    print('Not a moose')
elif l != r:
    print(f'Odd {2 * max(l, r)}')
else:
    print(f'Even {2 * l}')