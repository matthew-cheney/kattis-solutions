original = input()

moves = 0
for i, c in enumerate(original):
    if i % 3 == 0:
        moves += c != 'P'
    elif i % 3 == 1:
        moves += c != 'E'
    else:
        moves += c != 'R'

print(moves)