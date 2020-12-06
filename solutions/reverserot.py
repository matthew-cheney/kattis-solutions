char_to_num = {c: n for n, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')}

num_to_char = {n: c for n, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_.')}

while True:

    line = input()

    if line == '0':
        break

    line_l = line.split(' ')
    N = int(line_l[0])
    myList = list(line_l[1])[::-1]
    for i, c in enumerate(myList):
        myList[i] = num_to_char[char_to_num[c] + N]
    print(''.join(myList))
