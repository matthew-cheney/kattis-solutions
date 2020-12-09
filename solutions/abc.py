nums = [int(ea) for ea in input().split(' ')]

nums.sort()
d = {'A': nums[0],
     'B': nums[1],
     'C': nums[2]}

print(*[d[ea] for ea in input()])