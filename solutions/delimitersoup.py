L = input()
line = input()
line = list(line)
from collections import deque
closers = {')': '(',
           '}': '{',
           ']': '['}

s = deque()

valid = True
for i, delim in enumerate(line):
    if delim == ' ':
        continue
    if delim in closers:
        if len(s) > 0:
            stackTop = s.pop()
            if stackTop != closers[delim]:
                valid = False
                break
        else:
            valid = False
            break
    else:
        s.append(delim)

if not valid:
    print(delim, i)
else:
    print('ok so far')