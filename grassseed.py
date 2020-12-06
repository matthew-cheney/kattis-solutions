C = float(input())
L = int(input())
summer = 0
for i in range(L):
    line = input().split(' ')
    w, h = float(line[0]), float(line[1])
    summer += C * w * h
print(summer)