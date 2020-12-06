N = int(input())
nums = [int(ea) for ea in input().split(' ')]

last = -1
ans = []
for num in nums:
    if num > last:
        ans.append(num)
        last = num
print(len(ans))
print(*ans)
