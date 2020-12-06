X = int(input())
N = int(input())
months = []
for i in range(N):
    months.append(int(input()))

print(((N + 1) * X) - sum(months))