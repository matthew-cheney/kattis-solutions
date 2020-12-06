l, w = [int(x) for x in input().split(' ')]

if w > 26 * l or w < l * 1:
    print('impossible')
else:

    s = [1 for i in range(l)]

    to_change = len(s) - 1
    while sum(s) < w:
        if s[to_change] == 26:
            to_change -= 1
        s[to_change] += 1

    d = {i+1: v for i, v in enumerate(list('abcdefghijklmnopqrstuvwxyz'))}

    s_str = [d[c] for c in s]
    print(''.join(s_str))
