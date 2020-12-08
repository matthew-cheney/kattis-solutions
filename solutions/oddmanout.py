N = int(input())

for n in range(N):
    G = int(input())
    nums = input().split(' ')
    seen = set()
    for ea in nums:
        if ea in seen:
            seen.remove(ea)
        else:
            seen.add(ea)
    print(f'Case #{n+1}: {seen.pop()}')