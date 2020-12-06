import math
line = input().split(' ')
N = int(line[0])
W = int(line[1])
H = int(line[2])
dim = max(W, H, math.sqrt(W*W + H*H))
for i in range(N):
    if int(input()) <= dim:
        print("DA")
    else:
        print("NE")