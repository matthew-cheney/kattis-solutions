line = input().split(' ')
N = int(line[0])
D = line[1]

k = {
    'A': 11,
    'AD': 11,
    'K': 4,
    'KD': 4,
    'Q': 3,
    'QD': 3,
    'J': 20,
    'JD': 2,
    'T': 10,
    'TD': 10,
    '9': 14,
    '9D': 0,
    '8': 0,
    '8D': 0,
    '7': 0,
    '7D': 0
}  # got these vals reversed, so D == not dominant

score = 0
for n in range(N * 4):
    card = input().strip()
    val = card[0]
    suit = card[1]
    if suit != D:
        score += k[f'{val}D']
    else:
        score += k[val]

print(score)