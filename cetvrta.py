p1 = input().split(' ')
p2 = input().split(' ')
p3 = input().split(' ')

if p2[0] == p1[0]:
    print(p3[0], end=' ')
elif p2[0] == p3[0]:
    print(p1[0], end=' ')
else:
    print(p2[0], end=' ')

if p2[1] == p1[1]:
    print(p3[1])
elif p2[1] == p3[1]:
    print(p1[1])
else:
    print(p2[1])
