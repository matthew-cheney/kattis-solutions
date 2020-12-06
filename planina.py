N = int(input())
side_length = 2
for i in range(N):
    side_length = (2 * side_length) - 1
print(side_length ** 2)