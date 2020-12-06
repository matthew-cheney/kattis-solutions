N = int(input())

TB = 0
LR = 0
for n in range(N):
    T, B, L, R = [int(ea) for ea in list(input())]
    TB += not T
    TB += not B
    LR += not L
    LR += not R

limiting = min(TB, LR)
newSwords = limiting // 2
print(newSwords, TB - (2 * newSwords), LR - (2 * newSwords))