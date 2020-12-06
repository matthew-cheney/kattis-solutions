s = list(input())

# Divide
s1, s2 = s[:len(s) // 2], s[len(s) // 2:]

# Rotate
d = {v: i for i, v in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}
d2 = {i: v for i, v in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))}


sum1 = sum([d[c] for c in s1])
sum2 = sum([d[c] for c in s2])

s1 = [d2[(d[c] + sum1) % 26] for c in s1]
s2 = [d2[(d[c] + sum2) % 26] for c in s2]

# Merge
for i in range(len(s1)):
    s1[i] = d2[(d[s1[i]] + d[s2[i]]) % 26]

print(''.join(s1))