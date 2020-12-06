import sys
import math

lines = sys.stdin.readlines()

line = [float(ea) for ea in lines[0].split(' ')]
gopher = (line[0], line[1])
dog = (line[2], line[3])

holeFound = False
for line in lines[1:]:
    if line.strip() == '':
        continue
    x, y = [float(ea) for ea in line.split(' ')]
    gopherDist = math.sqrt((gopher[0] - x)**2 + (gopher[1] - y)**2)
    dogDist = math.sqrt((dog[0] - x)**2 + (dog[1] - y)**2)
    if dogDist >= gopherDist * 2:
        print(f'The gopher can escape through the hole at ({x:.3f},{y:.3f}).')
        holeFound = True
        break

if not holeFound:
    print('The gopher cannot escape.')