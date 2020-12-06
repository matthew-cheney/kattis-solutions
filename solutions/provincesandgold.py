victoryCards = [0]*2 + ['Estate']*3 + ['Duchy']*3 + ['Province']*15
moneyCards = ['Copper']*3 + ['Silver']*3 + ['Gold']*15

G, S, C = [int(ea) for ea in input().split(' ')]
money = 3 * G + 2 * S + C

if money < 2:
    print(moneyCards[money])
else:
    print(victoryCards[money], 'or', moneyCards[money])