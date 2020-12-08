line = input()
T, C, G = 0, 0, 0

for c in line:
    T += c == 'T'
    C += c == 'C'
    G += c == 'G'

print(T**2 + C**2 + G**2 + 7 * min(T, C, G))