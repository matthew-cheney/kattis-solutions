C, P = [int(ea) for ea in input().split(' ')]

partyVotes = []
partyBallot = []
totalVotes = 0
for p in range(P):
    line = [int(ea) - 1 for ea in input().split(' ')]
    partyVotes.append(line[0] + 1)
    totalVotes += (line[0] + 1)
    partyBallot.append([1] + line[1:])

eliminated = set()

winnerFound = False
while not winnerFound:
    candidateVotes = [0]*C
    # Count up votes for round
    for i, ballot in enumerate(partyBallot):
        candidateVotes[ballot[ballot[0]]] += partyVotes[i]

    # Find either winner of lowest candidate
    lowestVotesI = 0
    lowestVotes = 1000000000
    for i, votes in enumerate(candidateVotes):
        if i in eliminated:
            continue
        if votes > totalVotes // 2:
            print(i + 1)
            winnerFound = True
            break
        if votes < lowestVotes:
            lowestVotesI = i
            lowestVotes = votes

    eliminated.add(lowestVotesI)

    # Eliminate lowest candidate
    for ballot in partyBallot:
        while ballot[ballot[0]] in eliminated:
            ballot[0] += 1