a, b, c = [int(ea) for ea in input().split(' ')]

ops = ['+', '-', '*', '//']

ans = ''
for op in ops:
    s = f'{a}{op}{b}'
    if eval(s) == c:
        ans = s + f'={c}'
        break

if ans != '':
    print(ans.replace('//', '/'))
else:
    for op in ops:
        s = f'{b}{op}{c}'
        if eval(s) == a:
            ans = f'{a}=' + s
            break

    print(ans.replace('//', '/'))