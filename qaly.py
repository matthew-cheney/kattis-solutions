n = int(input())
summer = 0
for i in range(n):
    line = input().split(' ')
    q = float(line[0])
    y = float(line[1])
    summer += q * y
print(summer)