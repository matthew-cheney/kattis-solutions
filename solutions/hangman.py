word = input()
alpha = input()

wrongs = 0
for c in alpha:
    if c not in word:
        wrongs += 1
    else:
        word = word.replace(c, '')
    if len(word) == 0:
        break
    if wrongs == 10:
        break

if len(word) == 0:
    print('WIN')
else:
    print('LOSE')