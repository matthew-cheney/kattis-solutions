from queue import Queue
from collections import Counter

gatheringDay = False
days = Queue()
currentDay = ''
masterCounter = dict()
try:
    while True:
        line = input()
        if line == '' or line == '\n':
            continue
        if not gatheringDay and line.startswith('<text>'):
            gatheringDay = True
            line = line[6:]
        if gatheringDay:
            if line.strip() == '</text>':
                gatheringDay = False
                currentDayWords = currentDay.split()
                currentDayCounter = Counter([w for w in currentDayWords if len(w) >= 4])
                for k,v in currentDayCounter.items():
                    if k not in masterCounter:
                        masterCounter[k] = 0
                    masterCounter[k] += v
                days.put(currentDayCounter)
                currentDay = ''
                while days.qsize() > 7:
                    oldCounter = days.get()
                    for k,v in oldCounter.items():
                        masterCounter[k] -= v
                        if masterCounter[k] == 0:
                            masterCounter.pop(k)
                continue
            currentDay = currentDay + ' ' + line
            continue
        numWords = int(line.split(' ')[1])
        print(f'<top {numWords}>')

        vals = [(k, v) for k, v in masterCounter.items()]
        vals.sort(key=lambda x: (-x[1], x[0]))
        takeNext = 0
        prevFreq = -1
        wordsLeft = numWords
        while wordsLeft > 0 and takeNext < len(vals):
            wordsLeft -= 1
            print(vals[takeNext][0], vals[takeNext][1])
            prevFreq = vals[takeNext][1]
            takeNext += 1
        while takeNext < len(vals):
            if vals[takeNext][1] != prevFreq:
                break
            print(vals[takeNext][0], vals[takeNext][1])
            takeNext += 1
        print(f'</top>')
except EOFError:
    pass