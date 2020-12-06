N = int(input())
categories = dict()
for n in range(N):
    costume = input()
    if costume not in categories:
        categories[costume] = 0
    categories[costume] += 1

minValue = min(categories.values())
choices = [k for k, v in categories.items() if v == minValue]
choices.sort()
print(*choices, sep='\n')