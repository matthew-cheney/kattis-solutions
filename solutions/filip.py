line = input().split(' ')
x = int(line[0][::-1])
y = int(line[1][::-1])
print(max(x, y))