for n in range(int(input())):
    i = input()
    total = 0
    max_n = 0
    for c in range(1, len(i) + 1):
        total = str(bin(int(i[:c]))).count('1')
        max_n = max(max_n, total)
    print(max_n)