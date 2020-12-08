E, F, C = [int(ea) for ea in input().split(' ')]

B = E + F
total = 0
while B >= C:
    total += B // C
    B = B % C + B // C
print(total)