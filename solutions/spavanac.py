line = input().split(' ')
hours = int(line[0])
mins = int(line[1])

if mins < 45:
    hours -= 1
    if hours < 0:
        hours = 23
    mins = 60 - (45 - mins)
else:
    mins -= 45

print(hours, mins)