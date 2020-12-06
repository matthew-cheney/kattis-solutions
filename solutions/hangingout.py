line = input().split(' ')
L = int(line[0])
n = int(line[1])
on_terrace = 0
rejected = 0
for i in range(n):
    line = input().split(' ')
    g = int(line[1])
    if line[0] == 'enter':
        if on_terrace + g > L:
            rejected += 1
        else:
            on_terrace += g
    else:
        on_terrace -= g
print(rejected)
