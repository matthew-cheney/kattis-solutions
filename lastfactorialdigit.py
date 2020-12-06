import math

T = int(input())

for t in range(T):
    i = int(input())
    print(str(math.factorial(i))[-1])
