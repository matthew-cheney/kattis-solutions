import sys

lines = sys.stdin.readlines()

# lines = ['iBoard Rules!!']

for s in lines:

    s = s.rstrip('\n')

    if s == '':
        continue

    left = False
    right = False

    for c in s:
        b = ord(c)
        for i in range(7):
            target = b & 1
            if target:
                left = not left
            else:
                right = not right
            b >>= 1
    if left or right:
        print('trapped')
    else:
        print('free')