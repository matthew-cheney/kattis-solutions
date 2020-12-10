A, B, C = [int(ea) for ea in input().split(' ')]
print(max(abs(A - B), abs(B - C)) - 1)