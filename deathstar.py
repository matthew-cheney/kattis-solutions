import functools

N = int(input())
m = list()
nums = ''
for n in range(N):
    line = [int(x) for x in input().split(' ')]
    nums += functools.reduce(lambda x, y: x | y, line).__str__()
    nums += ' '

print(nums[:-1])
