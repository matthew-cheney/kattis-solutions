line = input().split(' ')
X, Y, N = int(line[0]), int(line[1]), int(line[2])
for i in range(1, N + 1):
    if i % X == 0:
        print('Fizz', end='')
    if i % Y == 0:
        print('Buzz', end='')
    if i % X != 0 and i % Y != 0:
        print(i, end='')
    print('')