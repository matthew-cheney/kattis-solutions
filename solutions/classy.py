T = int(input())

for t in range(T):
    N = int(input())
    people = []
    longest = 0
    for n in range(N):
        line = input().split(' ')
        c = line[1]
        c = c.replace('-', '')
        c = c.replace('upper', '1')
        c = c.replace('middle', '2')
        c = c.replace('lower', '3')
        longest = max(longest, len(c))
        c = c[::-1]
        people.append([line[0][:-1], c])
    for i in range(len(people)):
        while len(people[i][1]) < longest:
            people[i][1] += '2'
    people.sort(key=lambda x: (x[1], x[0]))
    print(*[x[0] for x in people], sep='\n')
    print('='*30)