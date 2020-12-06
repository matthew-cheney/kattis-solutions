import sys

N, Q = [int(x) for x in sys.stdin.readline().split(' ')]

T = [0]*(N + 1)

updates = dict()

for q in range(Q):
    line = sys.stdin.readline().split(' ')
    if line[0] == '+':
        # update
        ind = int(line[1])
        dif = int(line[2])
        if ind not in updates:
            updates[ind] = 0
        updates[ind] += dif
    else:
        # query
        # process updates first
        for ind, dif in updates.items():
            cur = ind + 1
            while cur < len(T):
                T[cur] += dif
                cur += cur & (-cur)
        updates = dict()
        cur = int(line[1])
        total_sum = 0
        while cur > 0:
            total_sum += T[cur]
            cur -= cur & (-cur)
        sys.stdout.write(str(total_sum) + '\n')
sys.stdout.flush()