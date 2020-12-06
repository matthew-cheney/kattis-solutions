T = int(input())
for t in range(T):
    N = int(input())
    cities = set()
    for n in range(N):
        cities.add(input())
    print(len(cities))