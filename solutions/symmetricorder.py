i = 1
while True:
    N = int(input())
    if N == 0:
        break
    print('SET', i)
    i += 1
    second = []
    for n in range(N // 2):
        print(input())
        second.append(input())
    if N % 2 != 0:
        print(input())
    print(*second[::-1], sep='\n')