N = int(input())

bases = list('0123456789abcdefghijklmnopqrstuvwxyz0')
chars = list('0123456789abcdefghijklmnopqrstuvwxyz')
charToInt = {c: i for i, c in enumerate(chars)}

def isValidBase(val: str, base: int):
    if base == 1:
        return set(val) == {'1'}
    else:
        return all([chars.index(c) < base for c in val])

def evalWithBase(val, base):
    res = 0
    for i in range(len(val)):
        res += charToInt[val[-(i + 1)]] * (base ** i)
    return res


for n in range(N):
    expr, ans = input().split('=')
    if '+' in expr:
        v1, v2 = expr.split('+')
        op = lambda x, y: x + y
    elif '-' in expr:
        v1, v2 = expr.split('-')
        op = lambda x, y: x - y
    elif '*' in expr:
        v1, v2 = expr.split('*')
        op = lambda x, y: x * y
    else:
        v1, v2 = expr.split('/')
        op = lambda x, y: x / y
    out = ''
    ans = ans.strip()
    v1 = v1.strip()
    v2 = v2.strip()
    for i in range(37):
        if not (isValidBase(v1, i) and isValidBase(v2, i) and isValidBase(ans, i)):
            continue
        if op(evalWithBase(v1, i), evalWithBase(v2, i)) == evalWithBase(ans, i):
            out += bases[i]
    print(out if len(out) > 0 else 'invalid')