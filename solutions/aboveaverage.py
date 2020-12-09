C = int(input())

for c in range(C):
    line = [int(ea) for ea in input().split(' ')]
    avg = sum(line[1:]) / line[0]
    aboves = [ea for ea in line[1:] if ea > avg]
    ans = len(aboves) / line[0]
    print(f'{100 * ans:0.3f}%')
