from collections import deque

N = int(input())

GOODS = {'$', '|', '*'}

COSTS = {'t': '|',
         'j': '*',
         'b': '$'}

for n in range(N):
    adv = input()
    stack = deque()
    success = True
    for c in adv:
        if c in GOODS:
            stack.append(c)
        elif c in COSTS:
            if len(stack) == 0 or stack.pop() != COSTS[c]:
                success = False
                break
    if len(stack) > 0:
        success = False
    print(('YES' if success else 'NO'))