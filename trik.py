line = input()
pos = 1

for c in line:
    if c == 'A':
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos = 1
    if c == 'B':
        if pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2
    if c == 'C':
        if pos == 1:
            pos = 3
        elif pos == 3:
            pos = 1

print(pos)