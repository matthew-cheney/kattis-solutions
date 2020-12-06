N = input()
line = input()
if line == '':
    print(0)
else:
    nums = [int(ea) for ea in line.split(' ')]
    print(-sum([ea for ea in nums if ea < 0]))