line = list(input())
new_line = []
skip = 0
for char in line[::-1]:
    if char == '<':
        skip += 1
        continue
    elif skip > 0:
        skip -= 1
        continue
    else:
        new_line.append(char)
print(''.join(new_line[::-1]))