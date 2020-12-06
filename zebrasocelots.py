N = int(input())

total = 0

for n in range(N):
    if input() == 'O':
        total += 2 ** ((N - 1) - n)

print(total)