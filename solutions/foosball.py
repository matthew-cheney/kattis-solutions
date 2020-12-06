from queue import Queue

N = int(input())
players = input().split(' ')
outcomes = list(input())

# [offense defense]
white = ['','']
black = ['','']

q = Queue()
for each in players:
    q.put(each)

white[0] = q.get()
black[0] = q.get()
white[1] = q.get()
black[1] = q.get()

streakTeams = []
highestStreak = 0
prevWinner = 'N'
currentStreak = 0

arrivedAtTable = {p: 0 for p in players}
arrivedAtTable[players[0]] = 1
arrivedAtTable[players[1]] = 2
arrivedAtTable[players[2]] = 3
arrivedAtTable[players[3]] = 4
arrivedAtTableCounter = 5

first = True
for outcome in outcomes:
    if outcome == 'W':
        winner = white
        loser = black
    else:
        winner = black
        loser = white
    # mark potentially record streak
    if not first and prevWinner != outcome:
        if currentStreak > highestStreak:
            highestStreak = currentStreak
            streakTeams = []
        if currentStreak >= highestStreak:
            if arrivedAtTable[loser[0]] < arrivedAtTable[loser[1]]:
                streakTeams.append((loser[0], loser[1]))
            else:
                streakTeams.append((loser[1], loser[0]))
        currentStreak = 0
    elif not first:
        currentStreak += 1
    first = False
    prevWinner = outcome
    q.put(loser[1])
    loser[1] = loser[0]
    loser[0] = q.get()
    arrivedAtTable[loser[0]] = arrivedAtTableCounter
    arrivedAtTableCounter += 1
    winner[0], winner[1] = winner[1], winner[0]

if outcome == 'W':
    loser = white
    winner = black
else:
    loser = black
    winner = white
if currentStreak > highestStreak:
    streakTeams = []
    highestStreak = currentStreak
if currentStreak >= highestStreak:
    if arrivedAtTable[loser[0]] < arrivedAtTable[loser[1]]:
        streakTeams.append((loser[0], loser[1]))
    else:
        streakTeams.append((loser[1], loser[0]))
for team in streakTeams:
    print(*team)