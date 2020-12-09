while True:
    num, dem = [int(ea) for ea in input().split(' ')]
    if num == 0 and dem == 0:
        break
    whole = num // dem
    num %= dem
    print(whole, num, '/', dem)