import heapq
import sys
from collections import deque

lines = sys.stdin.readlines()
nextLine = 0
while nextLine < len(lines):
    line = lines[nextLine]
    nextLine += 1
    if line.strip() == '':
        break
    N = int(line)
    if N == -1:
        break

    myStack = deque()
    myQueue = deque()
    myPriorityQueue = []

    isStack, isQueue, isPriorityQueue = True, True, True

    for n in range(N):
        line = lines[nextLine].strip().split(' ')
        nextLine += 1
        if line[0] == '1':
            numToAdd = int(line[1])
            myStack.append(numToAdd)
            myQueue.append(numToAdd)
            heapq.heappush(myPriorityQueue, -1 * numToAdd)
        else:
            targetNum = int(line[1])
            isStack = isStack and len(myStack) > 0 and myStack.pop() == targetNum
            isQueue = isQueue and len(myQueue) > 0 and myQueue.popleft() == targetNum
            isPriorityQueue = isPriorityQueue and len(myPriorityQueue) > 0 and heapq.heappop(myPriorityQueue) == targetNum * -1

    if sum([isStack, isQueue, isPriorityQueue]) == 0:
        print('impossible')
    elif sum([isStack, isQueue, isPriorityQueue]) > 1:
        print('not sure')
    else:
        if isStack:
            print('stack')
        elif isQueue:
            print('queue')
        elif isPriorityQueue:
            print('priority queue')