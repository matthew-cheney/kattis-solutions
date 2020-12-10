ranges = input().split(';')
total = 0
for r in ranges:
    if '-' in r:
        l = [int(ea) for ea in r.split('-')]
        total += (l[1] + 1) - l[0]
    else:
        total += 1
print(total)