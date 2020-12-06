N = int(input())

for n in range(N):
    K, W = [int(ea)for ea in input().split(' ')]
    masterString = ''
    for w in range(W):
        word = input()
        matchFound = False
        for i in range(len(word), -1, -1):
            if masterString.endswith(word[:i]):
                matchFound = True
                masterString += word[i:]
                break
        if not matchFound:
            masterString += word
    print(len(masterString))