while True:
    num_points = int(input())
    if num_points == 0:
        break
    polygon = list()
    for i in range(num_points):
        points = input().split(' ')
        polygon.append((int(points[0]), int(points[1])))
    polygon.append(polygon[0])

    adds = 0
    for i in range(len(polygon) - 1):
        adds += polygon[i][0] * polygon[i+1][1]
    negs = 0
    for i in range(len(polygon) - 1):
        negs += polygon[i][1] * polygon[i+1][0]
    area = (adds - negs) / 2
    if area < 0:
        direction = 'CW'
    else:
        direction = 'CCW'
    area = (area if area > 0 else -1 * area)

    print(f'{direction} {area:.01f}')