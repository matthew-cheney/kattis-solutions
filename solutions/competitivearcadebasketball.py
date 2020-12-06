N, P, M = [int(ea) for ea in input().split(' ')]

players = dict()

for n in range(N):
    players[input().strip()] = 0

winners = set()
podium = []

for m in range(M):
    name, score = input().split(' ')
    players[name] += int(score)
    if players[name] >= P and name not in winners:
        podium.append(name)
        winners.add(name)

if len(winners) == 0:
    print('No winner!')
else:
    for winner in podium:
        print(f'{winner} wins!')
