N = int(input())

count = 0
for n in range(N):
    line = input()
    if 'rose' in line.lower() or 'pink' in line.lower():
        count += 1

print(count if count > 0 else 'I must watch Star Wars with my daughter')