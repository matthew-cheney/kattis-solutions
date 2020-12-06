import sys

lines = sys.stdin.readlines()

for line in lines:

    if line.strip() == '':
        continue

    ints = [int(x) for x in line.split(' ')]

    big_sum = sum(ints)
    for my_int in ints:
        if big_sum - my_int == my_int:
            print(my_int)
            break