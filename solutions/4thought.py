M = int(input())

ops = ['*', '+', '-', '//']


def getAns():
    N = int(input())
    for o1 in ops:
        for o2 in ops:
            for o3 in ops:
                s = f'4 {o1} 4 {o2} 4 {o3} 4'
                if eval(s) == N:
                    print((s + ' = ' + str(N)).replace('//', '/'))
                    return
    print('no solution')


for m in range(M):
    getAns()