while True:
    n = int(input())
    if n == -1:
        break
    dist = 0
    prev_time = 0
    for i in range(n):
        line = input().split(' ')
        speed = int(line[0])
        time = int(line[1])
        dist += speed * (time - prev_time)
        prev_time = time
    print(dist, "miles")