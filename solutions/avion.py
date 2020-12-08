found = []

for i in range(1, 6):
    line = input()
    if 'FBI' in line:
        found.append(i)

if len(found) == 0:
    print('HE GOT AWAY!')
else:
    print(*found)