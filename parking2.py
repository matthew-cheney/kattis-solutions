T = int(input())

for t in range(T):
    N = input()
    stores = [int(ea) for ea in input().split(' ')]
    print(2 * (max(stores) - min(stores)))