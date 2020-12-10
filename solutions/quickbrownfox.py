N = int(input())

alphabet = set('abcdefghijklmnopqrstuvwxyz')

for n in range(N):
    msg = {ea for ea in input().lower() if ea in alphabet}
    if len(msg) == len(alphabet):
        print('pangram')
    else:
        print('missing', ''.join(sorted(alphabet - msg)))