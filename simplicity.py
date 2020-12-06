from collections import Counter
word = input()
C = Counter(word)
tot = 0
for k,v  in sorted(C.items(), key=lambda x: x[1], reverse=True)[2:]:
    tot += C[k]
print(tot)