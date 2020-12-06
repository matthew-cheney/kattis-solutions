import sys

lines = sys.stdin.readlines()

for line in lines:
    nums = [int(x) for x in line.split(' ')]
    diffs = [False for i in range(len(nums) - 1)]
    diffs[0] = True
    for i in range(len(nums) - 1):
        diff = abs(nums[i+1] - nums[i])
        if diff >= len(diffs):
            continue
        diffs[diff] = True
    print('Jolly' if all(diffs) else 'Not jolly')