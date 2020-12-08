N = int(input())

scores = []
for n in range(N):
    scores.append(int(input()))

def getScore(myScores):
    myTotal = 0
    for myI in range(len(myScores)):
        myTotal += myScores[myI] * ((4/5) ** myI)
    return myTotal / 5

print(getScore(scores))
total = 0
for i in range(len(scores)):
    total += getScore(scores[:i] + scores[i+1:])
print(total / len(scores))