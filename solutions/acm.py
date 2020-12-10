problemTimes = dict()
correctProblems = set()

while True:
    line = input()
    if line == '-1':
        break
    minute, problem, result = line.split(' ')
    if problem not in problemTimes:
        problemTimes[problem] = 0
    if result == 'right' and problem not in correctProblems:
        correctProblems.add(problem)
        problemTimes[problem] += int(minute)
    else:
        problemTimes[problem] += 20

print(len(correctProblems), sum([problemTimes[p] for p in correctProblems]))