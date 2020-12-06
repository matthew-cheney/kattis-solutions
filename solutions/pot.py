n = int(input())
summer = 0
for i in range(n):
    line = input()
    x = int(line[:-1])
    exp = int(line[-1])
    summer += x**exp
print(summer)