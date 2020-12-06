N = int(input())
visited = set()
for n in range(N):
    uni, team = input().split(' ')
    if len(visited) < 12 and uni not in visited:
        visited.add(uni)
        print(uni, team)
