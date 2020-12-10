N = int(input())

for n in range(N):
    S = int(input())
    segs = input().split(' ')
    reds = [int(ea[:-1]) for ea in segs if ea[-1] == 'R']
    blues = [int(ea[:-1]) for ea in segs if ea[-1] == 'B']
    reds.sort(reverse=True)
    blues.sort(reverse=True)
    if len(reds) == 0:
        print(f'Case #{n+1}: 0')
        continue
    elif len(blues) == 0:
        print(f'Case #{n+1}: 0')
        continue
    if reds[0] > blues[0]:
        first = reds
        second = blues
    else:
        first = blues
        second = reds
    fi, si = 0, 0
    length = 0
    segsUsed = 0
    while fi < len(first) and si < len(second):
        length += first[fi]
        length += second[si]
        segsUsed += 2
        fi += 1
        si += 1
    print(f'Case #{n+1}: {length - segsUsed}')