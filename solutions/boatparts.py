P, N = [int(ea) for ea in input().split(' ')]

partReplacements = set()

ans = -1
for n in range(1, N + 1):
    part = input()
    partReplacements.add(part)
    if len(partReplacements) == P:
        ans = n
        break
print(ans if ans > 0 else 'paradox avoided')