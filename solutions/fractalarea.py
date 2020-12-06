T = int(input())

cases = list()
for i in range(T):
    line = input().split(' ')
    cases.append((int(line[0]), int(line[1])))

pi = 3.141592653589793

for case in cases:
    r = case[0]
    n = case[1]
    if n == 1:
        print(pi * (r * r))
        continue
    if n == 2:
        area = (pi * (r * r))
        area += (pi * ((r/2) * (r/2))) * 4
        print(area)
        continue

    radii = [(r, 1)]
    new_radii = (r/2, 4)
    for i in range(n - 1):
        newer_radii = (new_radii[0]/2, new_radii[1]*3)
        radii.append(new_radii)
        new_radii = newer_radii
    area = 0
    for tup in radii:
        area += pi * (tup[0] * tup[0]) * tup[1]
    print(area)