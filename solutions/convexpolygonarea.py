num_polygons = int(input())

polygons = list()

for i in range(num_polygons):
    line = input().split(' ')
    num_points = int(line[0])
    c = 1
    new_polygon = list()
    for j in range(num_points):
        new_polygon.append((int(line[c]), int(line[c+1])))
        c += 2
    new_polygon.append(new_polygon[0])
    polygons.append(new_polygon)

for polygon in polygons:
    adds = 0
    for i in range(len(polygon) - 1):
        adds += polygon[i][0] * polygon[i+1][1]
    negs = 0
    for i in range(len(polygon) - 1):
        negs += polygon[i][1] * polygon[i+1][0]
    print((adds - negs) / 2)