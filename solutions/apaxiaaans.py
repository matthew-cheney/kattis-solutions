line = input()
prev = '$'
for c in line:
    if c != prev:
        print(c, end='')
    prev = c
print('')