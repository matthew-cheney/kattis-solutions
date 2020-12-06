N = int(input())
probs = list()
for n in range(N):
    line = input().split(' ')
    probs.append(float(line[1]))

probs.sort(reverse=True)

total = 0
for i, p in enumerate(probs):
    total += (i + 1) * p

print(total)