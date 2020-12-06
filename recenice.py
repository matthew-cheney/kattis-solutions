
hundreds = {'1': 'onehundred',
            '2': 'twohundred',
            '3': 'threehundred',
            '4': 'fourhundred',
            '5': 'fivehundred',
            '6': 'sixhundred',
            '7': 'sevenhundred',
            '8': 'eighthundred',
            '9': 'ninehundred'}

tens = {'2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety'}

smalls = {'1': 'one',
          '2': 'two',
          '3': 'three',
          '4': 'four',
          '5': 'five',
          '6': 'six',
          '7': 'seven',
          '8': 'eight',
          '9': 'nine',
          '10': 'ten',
          '11': 'eleven',
          '12': 'twelve',
          '13': 'thirteen',
          '14': 'fourteen',
          '15': 'fifteen',
          '16': 'sixteen',
          '17': 'seventeen',
          '18': 'eighteen',
          '19': 'nineteen'}

def intToLetters(n):
    numStr = ''
    if n > 99:
        numStr += hundreds[str(n)[0]]
        n -= 100 * int(str(n)[0])
    if n > 19:
        numStr += tens[str(n)[0]]
        n -= 10 * int(str(n)[0])
    if n > 0:
        numStr += smalls[str(n)]
    return numStr

def main():
    N = int(input())

    charCount = 0
    numIndex = 0
    words = []

    for n in range(N):
        word = input()
        if word == '$':
            numIndex = n
        else:
            charCount += len(word)
            words.append(word)

    if N == 1:
        print('four')
        return

    ans = ''
    for i in range(charCount, 1000):
        numStr = intToLetters(i)
        if charCount + len(numStr) == i:
            ans = i
            break

    print(*words[:numIndex], numStr, *words[numIndex:])

main()