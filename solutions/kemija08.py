encoded = input()
skip = 0
for c in encoded:
    if skip > 0:
        skip -= 1
        continue
    print(c, end='')
    if c in list('aeiou'):
        skip = 2
print('')