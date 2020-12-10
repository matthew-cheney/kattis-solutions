C = input()
K = input()

alphaPadded = '00000000000000000000000000ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(C)):
    offset = ord(K[i]) - 65
    if i % 2 == 0:
        print(alpha[alpha.index(C[i]) - offset], end='')
    else:
        print(alpha[alphaPadded.index(C[i]) + offset], end='')
print('')