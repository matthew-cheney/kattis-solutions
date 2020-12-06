N = int(input())

for n in range(N):
    line = input()
    if line[0] == 'P':
        print('skipped')
    else:
        line = line.split('+')
        print(int(line[0]) + int(line[1]))