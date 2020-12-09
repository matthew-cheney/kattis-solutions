K = int(input())

A, B = 1, 0

for k in range(K):
    A, B = B, A + B

print(A, B)