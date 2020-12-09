flips = {'1': '1',
         '2': '2',
         '5': '5',
         '6': '9',
         '8': '8',
         '9': '6',
         '0': '0'}

N, S = [int(ea) for ea in input().split(' ')]

nums = dict()

def canFlip(val):
    return all([c in flips for c in val])

def flip(val):
    return ''.join([flips[c] for c in val][::-1])

for ea in input().split(' '):
    if int(ea) not in nums:
        nums[int(ea)] = 0
    nums[int(ea)] += 1
    if canFlip(ea):
        newEa = flip(ea)
        if newEa == ea:
            continue
        if int(newEa) not in nums:
            nums[int(newEa)] = 0
        nums[int(newEa)] += 1

valid = False
for k in nums.keys():
    t = S - k
    if t in nums:
        if nums[t] > 1 or not canFlip(str(k)) or int(flip(str(k))) != t:
            valid = True
            break
print('YES' if valid else 'NO')