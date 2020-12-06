n = int(input())

while True:
    if n % sum([int(c) for c in str(n)]) == 0:
        print(n)
        break
    n += 1