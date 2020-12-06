import sys

lines = sys.stdin.readlines()
line = lines[0].split(' ')

P, T = int(line[0]), int(line[1])

opinions = [0 for i in range(P+1)]

for line in lines[1:]:
    if line.strip() == '':
        continue
    line = line.split(' ')
    p, t = int(line[0]), int(line[1])
    opinions[p] |= (1 << t)

print(len(set(opinions[1:])))