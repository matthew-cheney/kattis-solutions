points = []
for i in range(5):
    points.append([int(x) for x in input().split(' ')])
sums = [sum(line) for line in points]
max_i = sums.index(max(sums))
print(max_i + 1, sums[max_i])