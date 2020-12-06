from math import sqrt

T = int(input())

for t in range(T):
    encoded = input()
    sideLength = int(sqrt(len(encoded)))
    for i in range(sideLength):
        for j in range(sideLength):
            print(encoded[(sideLength - 1) + (j * sideLength) - i], end='')
    print('')
