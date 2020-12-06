while True:
    N = int(input())
    if N == 0:
        break
    ordersByFood = dict()
    for n in range(N):
        line = input().split(' ')
        for ea in line[1:]:
            if ea not in ordersByFood:
                ordersByFood[ea] = list()
            ordersByFood[ea].append(line[0])
    for k in sorted(ordersByFood.keys()):
        print(k, end=' ')
        print(*sorted(ordersByFood[k]))
    print('')
