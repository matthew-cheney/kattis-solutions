N = int(input())

nums = list()
for n in range(N):
    nums.append(input())

print(*nums[::-1], sep='\n')