N = input()
M = input()

out = []

decimalI = len(N) - len(M) + 1

if decimalI <= 0:
    out.append('0')

i = 0
while decimalI > 0:
    out.append(N[i])
    i += 1
    decimalI -= 1

out.append('.')
trueDecimalLocation = len(out) - 1

while decimalI < 0:
    out.append('0')
    decimalI += 1

out.extend(N[i:])

j = len(out) - 1
while j >= trueDecimalLocation:
    if out[j] != '0':
        break
    j -= 1

print(''.join(out[:j + (1 if j > trueDecimalLocation else 0)]))
