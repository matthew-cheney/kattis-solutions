while True:
    N = int(input())
    if N == 0:
        break
    collisions = dict()
    total_collisions = 0
    uniqueFiles = set()
    for n in range(N):
        file = input()
        uniqueFiles.add(file)
        filename = list(file)
        hash = ord(filename[0])
        for i in range(1, len(filename)):
            hash ^= ord(filename[i])
        if hash not in collisions:
            collisions[hash] = dict()
        if file not in collisions[hash]:
            collisions[hash][file] = 0
        collisions[hash][file] += 1
        # Add to total collisions
        total_collisions += sum([v for k, v in collisions[hash].items() if k != file])
    # print(collisions)
    print(len(uniqueFiles), total_collisions)