N = int(input())

trips = dict()

# Read in all the trips, group by country
for n in range(N):
    country, year = input().split(' ')
    if country not in trips:
        trips[country] = list()
    trips[country].append(int(year))

# Sort years within each country group
for k in trips.keys():
    trips[k].sort()

Q = int(input())

ans = []
for q in range(Q):
    country, i = input().split(' ')
    ans.append(trips[country][int(i)-1])

print(*ans, sep='\n')