N = int(input())

for n in range(N):
    w1 = input()
    w2 = input()
    wd = ''
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            wd += '.'
        else:
            wd += '*'
    print(w1)
    print(w2)
    print(wd)
    print('')