from collections import Counter

ranks = [ea[0] for ea in input().split(' ')]

c = Counter(ranks)

print(sorted(c.values(), reverse=True)[0])